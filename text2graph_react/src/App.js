import React, { useState, useEffect } from 'react';
import './App.css';
import './buffer_loading.css'


function App() {
  const [input1, setInput1] = useState('');
  const [input2, setInput2] = useState('');
  const [outputHtml, setOutputHtml] = useState('');
  const [isLoading, setIsLoading] = useState(false); // New loading state
    const [isGraphRendered, setIsGraphRendered] = useState(false);


    const createJSON = async () => {
        setIsLoading(true);
        const jsonOutput = JSON.stringify({ input1, input2 });
        console.log('Generated JSON:', jsonOutput);
        var outputHTMLString = await postData(input1);
        console.log('Posted input1:', outputHTMLString);
        setOutputHtml(outputHTMLString);

        executeScriptFromHtml(outputHTMLString);

        // Add this line to reset the input1 state
        setIsGraphRendered(true);
        setInput1(''); // This will clear the text in the textbox
    };
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
        setInput1(''); // This will clear the text in the textbox
    };

  useEffect(() => {
    if (outputHtml) {
      executeScriptFromHtml();
    }
  }, [outputHtml]);

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
    console.log('data:',data);
    setIsLoading(false);
    return data;
  } catch (error) {
    console.error('Error posting data:', error);
  }
};
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
            console.log('data:',data);
            setIsLoading(false);
            return data;
        } catch (error) {
            console.error('Error posting data:', error);
        }
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
                <label className="textLabel">Base Text</label>
                <textarea className="inputArea" value={input1} onChange={(e) => setInput1(e.target.value)} />
                {!isGraphRendered && (
                    <button className="jsonButton" onClick={createJSON}>Render Graph</button>
                )}
                {isGraphRendered && (
                    <button className="jsonButton" onClick={updateJSON}>Update Graph</button>
                )}

                {isGraphRendered && (
                <button className="resetButton" onClick={resetGraph}>Reset</button>
                )}
            </div>
            <div className="rightPanel">
                {rightPanelContent}
            </div>
        </div>
    </div>
);
}

export default App;
