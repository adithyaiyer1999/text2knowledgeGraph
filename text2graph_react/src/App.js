import React, { useState, useEffect } from 'react';
import './App.css';
// import loadingAnimationStyles from './buffer_loading.css'; // Import CSS for loading animation
// import loadingAnimationHtml from './buffer_loading.html'; // Import HTML for loading animation
import './buffer_loading.css'


function App() {
  const [input1, setInput1] = useState('');
  const [input2, setInput2] = useState('');
  const [outputHtml, setOutputHtml] = useState('');
  const [isLoading, setIsLoading] = useState(false); // New loading state


    const createJSON = async () => {
    setIsLoading(true);
    const jsonOutput = JSON.stringify({ input1, input2 });
    console.log('Generated JSON:', jsonOutput);
    var outputHTMLString = await postData(input1);
    console.log('Posted input1:', outputHTMLString);
    // outputHTMLString.replace('https://raw.githubusercontent.com/abhaykatheria/json2tree/main/J2T.png','./images/knowledgegraph.png')
    setOutputHtml(outputHTMLString);

    executeScriptFromHtml(outputHTMLString);
  };
  useEffect(() => {
    if (outputHtml) {
      executeScriptFromHtml();
    }
  }, [outputHtml]);

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
    // rightPanelContent = <div dangerouslySetInnerHTML={{ __html: loadingAnimationHtml }} />;
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
                <button className="jsonButton" onClick={createJSON}>Render Graph</button>
                <label className="textLabel">Additional Text </label>
                <textarea className="inputArea" value={input2} onChange={(e) => setInput2(e.target.value)} />
                <button className="jsonButton_update" onClick={createJSON}>Add text to Graph</button>
            </div>
            {/*<div className="rightPanel" dangerouslySetInnerHTML={{ __html: outputHtml }} />*/}
            <div className="rightPanel">
                {rightPanelContent}
            </div>
        </div>
    </div>
);
}

export default App;
