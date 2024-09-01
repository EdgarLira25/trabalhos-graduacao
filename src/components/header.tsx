import { useNavigate } from 'react-router-dom';
import { Button, HeaderContainer, Navegate } from './style';

const Header = () => {
    const navigate = useNavigate();

    const handleNavigateHome = () => {
        navigate('/query');
    };
    const handleNavigateTables = () => {
        navigate('/tables');
    };

    const handleNavigateExamples = () => {
        navigate('/examples');
    };

    return (
        <HeaderContainer>
            <Navegate>
                <Button onClick={handleNavigateHome}>
                    Realizar Consulta
                </Button>
                <Button onClick={handleNavigateExamples}>
                    Exemplos de Queries
                </Button>
                <Button onClick={handleNavigateTables}>
                    Tabelas do Database
                </Button>
            </Navegate>
        </HeaderContainer>
    );
};

export default Header;
