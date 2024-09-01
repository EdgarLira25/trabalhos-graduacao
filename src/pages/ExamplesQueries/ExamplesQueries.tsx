import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import { FiCopy } from 'react-icons/fi';
import { queries } from './consts';
import { Container, ContainerItem, ContainerList, Pre, Title } from './style';


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
        <Container>
            <Title>Lista de Queries</Title>
            <ContainerList>
                {queries.map((query, index) => (
                    <ContainerItem key={index}>
                        <Pre>
                            {query}
                        </Pre>
                        <FiCopy
                            onClick={() => copyToClipboard(query)}
                            style={{ marginLeft: '10px', marginRight: '10px', cursor: 'pointer' }}
                            size={24}
                        />
                    </ContainerItem>
                ))}
            </ContainerList>
            <ToastContainer />
        </Container >
    );
};

export default ExamplesQueries;
