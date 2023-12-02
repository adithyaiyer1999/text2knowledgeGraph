import React, { useState, useEffect } from 'react';
import './App.css';

function App() {
  const [input1, setInput1] = useState('');
  const [input2, setInput2] = useState('');
  const [outputHtml, setOutputHtml] = useState('');

  const createJSON = async () => {
    const jsonOutput = JSON.stringify({ input1, input2 });
    console.log('Generated JSON:', jsonOutput);
    var outputHTMLString = await postData(input1);
    console.log('Posted input1:', outputHTMLString);

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
    return data;
  } catch (error) {
    console.error('Error posting data:', error);
  }
};

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
            <div className="rightPanel" dangerouslySetInnerHTML={{ __html: outputHtml }} />
        </div>
    </div>
);
}

export default App;
