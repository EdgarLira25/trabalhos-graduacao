import React, { useState } from 'react';
import axios from 'axios';

const SqlQuery: React.FC = () => {
    const [query, setQuery] = useState<string>('');
    const [response, setResponse] = useState<string>('');

    const handleInputChange = (event: React.ChangeEvent<HTMLTextAreaElement>) => {
        setQuery(event.target.value);
    };

    const handleSubmit = async (event: React.FormEvent) => {
        event.preventDefault();

        try {
            const res = await axios.get('http://127.0.0.1:8000/query', { params: { query } });
            setResponse(res.data.replace(/\n/g, '\n'));
        } catch (error) {
            setResponse(`Error: ${error}`);
        }
    };

    return (
        <div style={{ padding: '20px' }}>
            <h1>SQL Query Executor</h1>
            <form onSubmit={handleSubmit}>
                <textarea
                    value={query}
                    onChange={handleInputChange}
                    rows={10}
                    cols={50}
                    placeholder="Write your SQL query here..."
                />
                <br />
                <button type="submit" style={{ marginTop: '10px' }}>Execute Query</button>
            </form>
            <h2>Response:</h2>
            <pre>{response}</pre>
        </div>
    );
};

export default SqlQuery;
