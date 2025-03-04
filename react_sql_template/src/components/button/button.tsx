import { Button } from "./style";

interface Props {
    loading: boolean;
    children: any;
}
// Componente Button
const LoadingButton = ({ loading, children }: Props) => {
    return (
        <Button type="submit" disabled={loading}>
            {children}
            {loading && <div className="spinner" />}
        </Button>
    );
};

export default LoadingButton;
