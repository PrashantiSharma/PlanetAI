import React, { useState } from "react";
import "./App.css";
import ChatSection from "./components/chatsection";
import uploadpic from './img/uploadpdf.png';
import logo from './img/logo.png';
import file_pic from './img/file.png';

function App() {
  const [file, setFile] = useState(null);

  const handleFileUpload = async (event) => {
    const selectedFile = event.target.files[0];
    setFile(selectedFile);

    const formData = new FormData();
    formData.append("file", selectedFile);

    try {
      const response = await fetch("http://127.0.0.1:8000/upload-pdf", {
        method: "POST",
        body: formData,
      });

      if (response.ok) {
        const result = await response.json();
        console.log("Uploaded file:", result);
        alert(`File uploaded successfully`);
      } else {
        console.error("Failed to upload file:", response.statusText);
      }
    } catch (error) {
      console.error("Error during file upload:", error);
    }
  };

  return (
    <div className="App">
      {/* Header Section */}
      <header className="app-header">
        <div className="logo">
          <img src={logo} alt="Logo" className="logo-img" />
        </div>
        
        {/* Display file name next to the upload button */}
        <div className="upload-container">
          {file && (
            <div className="file-name" >
              <img src={file_pic} alt="File:" className="file-pic" />
              {file.name}
            </div>
          )}

          <label htmlFor="file-upload" className="upload-label">
            <img src={uploadpic} alt="Upload Icon" className="upload-icon" />
          </label>
          <input
            type="file"
            id="file-upload"
            accept="application/pdf"
            onChange={handleFileUpload}
            style={{ display: "none" }}
          />
        </div>
      </header>
      
      <main className="main-content">
        <ChatSection />
      </main>
    </div>
  );
}

export default App;

