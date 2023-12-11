import React, { useState, useEffect } from 'react';
import './App.css';
import './buffer_loading.css'

function App() {
  const [input1, setInput1] = useState('');
  const [input2, setInput2] = useState('');
  const [outputHtml, setOutputHtml] = useState('');
  const [isLoading, setIsLoading] = useState(false); // New loading state
  const [isGraphRendered, setIsGraphRendered] = useState(false);
  const [fileName, setFileName] = useState("");
  const [searchText, setSearchText] = useState("");
  const [bigGraph, setbigGraph] = useState("{}");
  const [pdfFile, setPdfFile] = useState(null);

    const handleRenderGraph = () => {
        if (pdfFile) {
            sendPdfFileToBackend();  // Function to handle PDF file upload
        } else {
            createJSON();  // Function to process text input
        }
    };

const handleFileChange = (e) => {
    const file = e.target.files[0];
    if (file) {
        const fileType = file.name.split('.').pop();

        if (fileType === 'txt') {
            setFileName(file.name);
            const reader = new FileReader();
            reader.onload = (e) => {
                setInput1(e.target.result);
            };
            reader.readAsText(file);

        } else if (fileType === 'pdf') {
            // Handle pdf file (e.g., set state for PDF file)
            setFileName(file.name);
            setPdfFile(file);
        }
    }
};

    // Create JSON format
    const createJSON = async () => {
      setIsLoading(true);
      const jsonOutput = JSON.stringify({ input1, input2 });
      console.log('Generated JSON:', jsonOutput);
      try{
        var outputHTMLString = await postData(input1);
      } catch (error) {
        console.error('Error posting data:', error);
      }
      
      console.log('Posted input1:', outputHTMLString);
      setOutputHtml(outputHTMLString);

      executeScriptFromHtml(outputHTMLString);

      // Add this line to reset the input1 state
      setIsGraphRendered(true);
      // setInput1(''); // This will clear the text in the textbox # Adi - We don't wanna do this? Makes it visaually unappealing
  };

  const reload = async () => {
    setOutputHtml(bigGraph);
    executeScriptFromHtml(bigGraph);

    // setInput1(''); // This will clear the text in the textbox # Adi - We don't wanna do this? Makes it visaually unappealing
};

    // Update the JSON format
    const updateJSON = async () => {
        setIsLoading(true);
        const jsonOutput = JSON.stringify({ input1, input2 });
        console.log('Generated JSON:', jsonOutput);
        var outputHTMLString = await updateData(input1);
        console.log('Posted input1:', outputHTMLString);
        setOutputHtml(outputHTMLString);

        executeScriptFromHtml(outputHTMLString);

        // Add this line to reset the input1 state
        setIsGraphRendered(true);
        // setInput1(''); // This will clear the text in the textbox, # Adi - lets not do this
    };

    // Search the JSON format
    // Update the JSON format
    const searchJSON = async () => {
      setIsLoading(true);

      var outputHTMLString = await searchData(searchText);
      console.log('Returned data post search', outputHTMLString);
      setOutputHtml(outputHTMLString);

      executeScriptFromHtml(outputHTMLString);

      // Add this line to reset the input1 state
      setIsGraphRendered(true);
      // setInput1(''); // This will clear the text in the textbox, # Adi - lets not do this
  };
    
    // Use the javascript to build bueatiful visualizations
  useEffect(() => {
    if (outputHtml) {
      executeScriptFromHtml();
    }
  }, [outputHtml]);
  
  // Reset the graph to Null State
    const resetGraph = () => {
        setIsGraphRendered(false);
        setOutputHtml('');
        setInput1('');
        // If you need to reset input2 as well, uncomment the following line
        // setInput2('');
    };

  
  const executeScriptFromHtml = () => {
    var toggler = document.getElementsByClassName("caret");
    for (let i = 0; i < toggler.length; i++) {
      toggler[i].addEventListener("click", function() {
        this.parentElement.querySelector(".nested").classList.toggle("active");
        this.classList.toggle("caret-down");
      });
    }
  };

  
  // Api call to create graph from text
  const postData = async (dataToSend) => {
      console.log("Data reached in:", dataToSend)
  try {
    const response = await fetch('http://127.0.0.1:8000/api/create-graph-from-text/', {
      method: 'POST',
        credentials: 'include',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        text : dataToSend
      }),
    });

    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }

    console.log('response:',response);
    const data = await response.text();
    setbigGraph(data);
    console.log('data:',data);
    setIsLoading(false);
    return data;
  } catch (error) {
    console.error('Error posting data:', error);
  }
};

  // API call to update data
  const updateData = async (dataToSend) => {
        console.log("Data reached in:", dataToSend)
        try {
            const response = await fetch('http://127.0.0.1:8000/api/add-to-graph-from-text/', {
                method: 'POST',
                credentials: 'include',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    text : dataToSend
                }),
            });

            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }

            console.log('response:',response);
            const data = await response.text();
            
            setbigGraph(data);
            console.log('data:',data);
            setIsLoading(false);
            return data;
        } catch (error) {
            console.error('Error posting data:', error);
        }
    };

  // API call to search graph
  const searchData = async (dataToSend) => {
      console.log("Data reached in:", dataToSend)
      try {
          const response = await fetch('http://127.0.0.1:8000/api/search-graph-from-text/', {
              method: 'POST',
              credentials: 'include',
              headers: {
                  'Content-Type': 'application/json',
              },
              body: JSON.stringify({
                  text : dataToSend
              }),
          });

          if (!response.ok) {
              throw new Error(`HTTP error! Status: ${response.status}`);
          }

          console.log('response:',response);
          const data = await response.text();
          console.log('data:',data);
          setIsLoading(false);
          return data;
      } catch (error) {
          console.error('Error posting data:', error);
      }
  };

  const sendPdfFileToBackend = async (e) => {
      setIsLoading(true);
      const formData = new FormData();
      formData.append('file', pdfFile);
      const response = await fetch('http://127.0.0.1:8000/api/create-graph-from-pdf/', {
          method: 'POST',
          body: formData,
      });
    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }
    console.log('response:',response);
    const data = await response.text();
    setIsLoading(false);
    console.log('data:',data);
    setOutputHtml(data);
    executeScriptFromHtml(data);
    setIsGraphRendered(true);
  };
  
  
  
let rightPanelContent;
if (isLoading) {
    rightPanelContent = (
        <div className='container'>
            <div className='loader'>
                <div className='loader--dot'></div>
                <div className='loader--dot'></div>
                <div className='loader--dot'></div>
                <div className='loader--dot'></div>
                <div className='loader--dot'></div>
                <div className='loader--dot'></div>
                <div className='loader--text'></div>
            </div>
        </div>
    );
} else {
    rightPanelContent = <div dangerouslySetInnerHTML={{ __html: outputHtml }} />;
}

  return (
    <div className="App">
        <h1 className="title">Graph Your Story</h1>
        <div className="content">
            <div className="leftPanel">
                <label className="textLabel">Enter Your Text</label>
                <textarea className="inputArea" value={input1} onChange={(e) => setInput1(e.target.value)} />

                {!isGraphRendered && (
                    <div className="orSeparator">OR</div>
                )}
                {!isGraphRendered && (
                    <label htmlFor="file-upload" className="custom-file-upload">Upload PDF or TXT File</label>
                )}
                {!isGraphRendered && (
                    <input id="file-upload" type="file" accept=".txt, .pdf" onChange={handleFileChange} style={{ display: 'none' }} />

            )}

                {fileName && <span className="file-name">{fileName}</span>}
                {!isGraphRendered && (
                    <button className="jsonButton" onClick={handleRenderGraph}>Render Graph</button>
                )}
                {isGraphRendered && (
                    <button className="jsonButton" onClick={updateJSON}>Update Graph</button>
                )}

                {isGraphRendered && (
                <button className="resetButton" onClick={resetGraph}>Reset</button>
                )}
            </div>
            <div className="rightPanel">
            <div className="searchBar">
        <input
          className="searchInput"
          type="text"
          value={searchText}
          onChange={(e) => setSearchText(e.target.value)}
          placeholder="Search..."
        />
    <button className="searchButton" onClick={() => searchJSON(searchText)}>Search</button>
    <button className="reloadButton" onClick={() => reload()}>Reload main graph</button>
</div>
                {rightPanelContent}
            </div>
        </div>
    </div>
);
}

export default App;
