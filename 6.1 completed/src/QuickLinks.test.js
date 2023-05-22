import { render, screen } from '@testing-library/react';
import  UserList from './UserList';

describe('quick links test', () => {
    test ('shows covid 19 link when specialty is General Medical', ()=> {
        //render component
        render(<UserList specialty="General Medical" />);
    
        //find the covid link by text
        const link = screen.getByText("Covid-19 Guidelines");
    
        // assertion
        expect(link).toBeInTheDocument();
    });
    
    test ('does not shows covid 19 link when specialty is not General Medical', ()=> {
        //render component
        render(<UserList specialty="Not general medical" />);
        //find the covid
        const link = screen.getByText("Covid-19 Guidelines");
        // assertion
        console.log("Component ", )
        console.log("Link ", link);
        expect(link).not.toBeInTheDocument();
    });
    
    test ('it shows provider resources link', ()=> {
        //render component
        render(<UserList />);
        //provider resources link
        const link = screen.getByText("Provider Resources");
        // assertion
        expect(link).toBeInTheDocument();
    });
})
