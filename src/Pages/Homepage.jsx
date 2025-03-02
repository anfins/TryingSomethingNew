import React, {  useState } from "react";
import "./Homepage.css";
import axios from "axios";

const Homepage = () => {
  const [userInput, setUserInput] = useState("");
  const [result, setResult] = useState("");
  const handleClick = async () => {
    /**
     * This function sends the playerInput to the server and gets the result
     * The result is then set to the result state
     */
    try {
      //Send playerInput to the server at PORT 5000 and gets the result
      console.log("something")
      const response = await axios.post("http://localhost:5000/run-python", {
        userInput,
      });
      setResult(response.data.result);
    } catch (error) {
      console.log("something else")
      console.error("Error calling Python script:", error);
    }
  };

  return (
    <div className="container">
      <div className="content">
        <h1 className="title">Enter Query</h1>
        <div className="input-container">
          <input
            type="text"
            placeholder="Enter text..."
            onChange={(e) => setUserInput(e.target.value)}
            className="input-field"
          />
          <button className="submit-button" onClick={handleClick}>
            Submit
          </button>
        </div>
      </div>
      {result && (
        <div className="results-container">
          <h2>Results:</h2>
          <p>{result}</p>
        </div>
      )}
    </div>
  );
};

export default Homepage;
