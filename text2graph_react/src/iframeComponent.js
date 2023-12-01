import React from 'react';

function IframeComponent() {
  return (
    <iframe 
      src="/Users/adithyaiyer/Desktop/llvm-project/text2graph_react/public/output.html" // Replace with your HTML file path
      title="My HTML Content"
      width="100%"
      height="600px"
      style={{ border: 'none' }} // Optional: to remove iframe border
    ></iframe>
  );
}

export default IframeComponent;
