import { isAxiosError } from 'axios';
import React, { useState } from 'react';
import api from '../api/api';

const SqlQuery: React.FC = () => {
    const [query, setQuery] = useState<string>('');
    const [response, setResponse] = useState<string>('');

    const handleInputChange = (event: React.ChangeEvent<HTMLTextAreaElement>) => {
        setQuery(event.target.value);
    };

    const handleSubmit = async (event: React.FormEvent) => {
        event.preventDefault();

        try {
            const res = await api.get('/query', { params: { query } });
            setResponse(res.data.replace(/\n/g, '\n'));
        } catch (error) {
            if (isAxiosError(error)) {
                if (error.response) {
                    setResponse(`Error: ${error.response.data}`);
                    if (error.response.data === "no results to fetch") setResponse(`Engraçadinho você em, só aceitamos SELECT`);
                    return
                }
            }
            setResponse(`Error: ${error}`)
        }
    };

    return (
        <div
            style={{
                display: 'flex',
                flexDirection: 'column',
                alignItems: 'center',
                justifyContent: 'center',
            }}
        >
            <h1>SQL</h1>
            <form onSubmit={handleSubmit}>
                <textarea
                    value={query}
                    onChange={handleInputChange}
                    rows={10}
                    cols={50}
                    placeholder="Escreva sua consulta SQL"
                />
                <br />
                <button type="submit" style={{ marginTop: '10px', display: 'flex', justifyContent: 'center', flexDirection: 'column' }}>Executar Query</button>
            </form>
            <h2>Resultado</h2>
            <pre>{response}</pre>
        </div>
    );
};

export default SqlQuery;
