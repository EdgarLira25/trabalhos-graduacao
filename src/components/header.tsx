import { useNavigate } from 'react-router-dom';
import { Button, HeaderContainer, Navegate } from './style';

const Header = () => {
    const navigate = useNavigate();

    const handleNavigateHome = () => {
        navigate('/query');
    };

    return (
        <HeaderContainer>
            <Navegate>
                <Button onClick={handleNavigateHome}>
                   Realizar Consulta 
                </Button>
            </Navegate>
        </HeaderContainer>
    );
};

export default Header;
