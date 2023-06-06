import React from 'react';
import { shallow, mount, render } from 'enzyme';
import { expect } from 'test';

import { MiddleTier } from './MiddleTier';

describe('Verify MiddleTier component', () => {

    it('should render Middletier Component', () => {
        expect(shallow(<MiddleTier />).length).toEqual(1);
    });

    it('should match snapshot', () => {
        expect(shallow(<MiddleTier />).toMatchSnapshot());
    });

    it('should have correct state', () => {
        const state = {
            isOpen: false,
            showConfirmExit: false,
            showHelp: false
        };
        const wrapper = shallow(<MiddleTier />);
        expect(wrapper.state()).toEqual(state);

    });

    it('renders MobileNav if isOpen is true', () => {
        const wrapper = shallow(<MiddleTier />); // isOpen should be false
        expect(wrapper.find('MobileNav').length).toEqual(0);

        setState({ isOpen: !state.isOpen }); // isOpen is now true
        expect(wrapper.find('MobileNav').length).toEqual(1);
    });

    it('should have topdanmark links', () => {
        const wrapper = shallow(<MiddleTier />);
        const navlinks = wrapper.find('NavLink');  // find all NavLink tags, expect 4
        const topdanmark_blank = wrapper.find('NavLink[target="_blank"]'); // find all NavLink tags with "_blank" target properties, expect 2
        const topdanmark_href = wrapper.find('NavLink[href="groupHomepageUrl"]'); // find all NavLink tags with groupHomepageUrl, expect 2
        topdanmark_href.forEach(navLink => expect(navLink.find('img[src="navLogo("topdanmark_secondary")]'))) // navlinks should have child img tag with src of whatever navLogo('topdanmark_secondary') returns
    });

});
