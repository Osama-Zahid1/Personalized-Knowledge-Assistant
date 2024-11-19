// src/ChatComponent.js
import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

const ChatComponent = () => {
    const [query, setQuery] = useState('');
    const [response, setResponse] = useState('');
    const [error, setError] = useState('');
    const [showForm, setShowForm] = useState(false);

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const res = await axios.post('http://localhost:8000/api/chat/', { query });
            setResponse(res.data.response);
            setError('');
        } catch (err) {
            setError('Error: ' + err.response?.data?.error || err.message);
            setResponse('');
        }
    };

    const handleFormToggle = () => {
        setShowForm(true); // Show the form when button is clicked
    };

    return (
        <div className="chat-container">
            {!showForm && (
                <button className="open-button" onClick={handleFormToggle}>
                    Ask Me Anything
                </button>
            )}

            {showForm && (
                <div className="form-container show">
                    <div className="form-content">
                        <h2>Ask a Question</h2>
                        <form onSubmit={handleSubmit}>
                            <input
                                type="text"
                                value={query}
                                onChange={(e) => setQuery(e.target.value)}
                                placeholder="Enter your query"
                            />
                            <button type="submit">Submit</button>
                        </form>
                        {response && <p>Response: {response}</p>}
                        {error && <p style={{ color: 'red' }}>{error}</p>}
                    </div>
                </div>
            )}

            {showForm && (
                <button className="ask-again" onClick={() => setShowForm(false)}>
                    Ask Me Anything Again
                </button>
            )}
        </div>
    );
};

export default ChatComponent;