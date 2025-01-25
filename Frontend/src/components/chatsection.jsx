import React, { useState } from 'react';
import './ChatSection.css';
import userIcon from '../img/User.png';
import replyIcon from '../img/reply.png';
import arrow from '../img/arrow.png';

const ChatSection = () => {
  const [message, setMessage] = useState('');
  const [messages, setMessages] = useState([]);
  const [file, setFile] = useState(null); // File state to handle file upload

  // Function to handle file selection
  const handleFileUpload = (event) => {
    setFile(event.target.files[0]);
    console.log("Uploaded file:", event.target.files[0]);
  };

  const sendMessage = async () => {
    if (message.trim() === '') return; // Prevent empty messages
  
    // Add user message to the chat
    setMessages((prevMessages) => [
      ...prevMessages,
      { text: message, sender: 'user' },
    ]);
  
    try {
      // Prepare the form data
      const formData = new FormData();
      formData.append('question', message);
  
      for (let [key, value] of formData.entries()) {
        console.log(key, value);
      }
      
  
      // Send the form data to the backend
      const response = await fetch('http://127.0.0.1:8000/ask', {
        method: 'POST',
        body: formData, // Sending the data as form-data for file upload
      });
  
      if (response.ok) {
        const data = await response.json();
        const aiResponse = data.answer;
  
        // Add AI response to the chat
        setMessages((prevMessages) => [
          ...prevMessages,
          { text: aiResponse, sender: 'ai' },
        ]);
      } else {
        console.error('Failed to get a response from the backend:', response);
      }
    } catch (error) {
      console.error('Error communicating with the backend:', error);
    }
  
    // Clear input field
    setMessage('');
  };
  

  return (
    <div className="chat-section">
      {/* Chat Messages */}
      <div className="chat-messages">
        {messages.map((msg, index) => (
          <div key={index} className="whole-message">
            <img
              src={msg.sender === 'user' ? userIcon : replyIcon}
              alt={msg.sender === 'user' ? 'User' : 'AI'}
              className="user-icon"
            />
            <div className={`message ${msg.sender}`}>{msg.text}</div>
          </div>
        ))}
      </div>

      {/* File Upload */}
      <div className="file-upload">
        <input
          type="file"
          id="file-upload"
          accept="application/pdf"
          onChange={handleFileUpload}
        />
      </div>

      {/* Chat Input */}
      <div className="chat-input">
        <input
          type="text"
          placeholder="Send A Message..."
          value={message}
          onChange={(e) => setMessage(e.target.value)}
          onKeyDown={(e) => e.key === 'Enter' && sendMessage()}
        />
        <button onClick={sendMessage} className="send-button">
          <img src={arrow} alt="Send" className="send-icon" />
        </button>
      </div>
    </div>
  );
};

export default ChatSection;
