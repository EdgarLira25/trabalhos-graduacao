import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import { FiCopy } from 'react-icons/fi';
import { queries } from './consts';


const copyToClipboard = (text: string) => {
    navigator.clipboard.writeText(text).then(() => {
        toast.success('Query copiada para a área de transferência!', {
            position: "bottom-center",
            autoClose: 2000,
            hideProgressBar: true,
            closeOnClick: true,
            pauseOnHover: false,
            draggable: true,
            progress: undefined,
        });
    });
};

const ExamplesQueries = () => {
    return (
        <div style={{ padding: '20px' }}>
            <h1>Lista de Queries</h1>
            <div style={{ maxHeight: '650px', overflowY: 'auto', padding: '10px' }}>
                <ul style={{ listStyleType: 'none', padding: 0 }}>
                    {queries.map((query, index) => (
                        <li key={index} style={{ marginBottom: '20px' }}>
                            <div style={{ display: 'flex', alignItems: 'center' }}>
                                <pre style={{
                                    backgroundColor: '#f4f4f4',
                                    padding: '10px',
                                    borderRadius: '5px',
                                    margin: 0,
                                    overflowX: 'auto',
                                    maxWidth: '600px',
                                    whiteSpace: 'pre-wrap',
                                    wordWrap: 'break-word',
                                    flex: 1
                                }}>
                                    {query}
                                </pre>
                                <FiCopy
                                    onClick={() => copyToClipboard(query)}
                                    style={{ marginLeft: '10px', cursor: 'pointer' }}
                                    size={24}
                                />
                            </div>
                        </li>
                    ))}
                </ul>
            </div>
            <ToastContainer />
        </div >
    );
};

export default ExamplesQueries;
