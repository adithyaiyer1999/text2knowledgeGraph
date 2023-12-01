import React, { Component } from 'react';

class MyComponent extends Component {
  render() {
    return (
        <iframe 
        src="../public/output.html"
        title="My HTML Content"
        width="100%"
        height="600px"
      ></iframe>
    );
  }
}

export default MyComponent;
