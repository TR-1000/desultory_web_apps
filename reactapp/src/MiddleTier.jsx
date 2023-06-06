import React, { Component } from 'react';
import PropTypes from 'prop-types';
import classNames from 'classnames';
import { MobileNav } from '../shared/mobile-nav/mobile-nav';
import { NavbarDropdown, NavItem, NavLink } from '../nav-components';
import { ConfirmModal, HelpModal } from '../../modals';
import LocaleContainer from '../../LocaleDropdown/containers/LocaleContainer';

import { LogoutIcon, MenuIcon } from 'app/icon-web';
import { navLogo } from '../shared/nav-logo';
import { I18n, translate } from '@td/shared_utils';

const ariaLabels = {
    help: translate(null, 'navigation_menu.middle-tier.help', 'aria_label'),
    menu: translate(null, 'navigation_menu.middle-tier.menu', 'label')
};
const altLogo = translate(null, 'navigation_menu.middle-tier.logo', 'label');
const altLogoTeladoc = translate(null, 'navigation_menu.middle-tier.teladoc_logo', 'label');

class MiddleTier extends Component {
    constructor(props) {
        super(props);
        this.iconRef = React.createRef();
    }

    state = {
        isOpen: false,
        showConfirmExit: false,
        showHelp: false
    };

    confirmLogout = () => this.setState({ showConfirmExit: true });
    cancelLogout = () => this.setState({ showConfirmExit: false });
    displayHelp = () => this.setState({ showHelp: true });
    exitHelp = () => this.setState({ showHelp: false });
    logout = () => window.location.replace('/logout');
    toggleMenu = () => {
        this.setState({ isOpen: !this.state.isOpen });
        setTimeout(() => {
            const firstEl = document.querySelector('.first-link');
            firstEl.focus();
        }, 50);
    };

    render() {
        const { isOpen, showConfirmExit, showHelp } = this.state;
        const {
            memberId,
            myFamily,
            brandCode,
            groupHomepageUrl,
            isImpersonationActive,
            impersonationRestrictions,
            groupHasEMO2Access,
            tollfreeNumber
        } = this.props;
        const { allowAuthorizedConsenter, allowCareRecipients } = myFamily;

        return (
            <div className={classNames('row middle-tier', { isOpen })}>
                <div className="container">
                    {isOpen ? (
                        <MobileNav
                            memberId={memberId}
                            brandCode={brandCode}
                            toggleMenu={this.toggleMenu}
                            iconRef={this.iconRef}
                            isExpanded={this.state.isOpen}
                            expandMenu={this.toggleMenu}
                            collapseMenu={this.toggleMenu}
                            allowAuthorizedConsenter={allowAuthorizedConsenter}
                            allowCareRecipients={allowCareRecipients}
                            isImpersonationActive={isImpersonationActive}
                            impersonationRestrictions={impersonationRestrictions}
                            groupHasEMO2Access={groupHasEMO2Access}
                            showMessageCounter
                            showCaseHistory
                            showLocaleContainer
                        />
                    ) : null}


                    <div className={classNames('row nav-wrapper', { isOpen })}>
                        <NavbarDropdown className="dropdown navbar-nav menu-icon">
                            
                            <NavItem onClick={this.toggleMenu}>
                                <NavLink className="first-link" role="button" aria-label={ariaLabels.menu}>
                                    <MenuIcon />
                                </NavLink>
                            </NavItem>



                            <NavItem>
                                <img src={navLogo(brandCode)} alt={altLogo} className="mobile-logo header-logo" />
                            </NavItem>



                            <NavItem className="logo-secondary">
                                <NavLink href={groupHomepageUrl} target="_blank" rel="noopener noreferrer">
                                    <img src={navLogo('topdanmark_secondary')} alt={altLogo} className="mobile-logo header-logo" />
                                </NavLink>
                            </NavItem>




                        </NavbarDropdown>
                        <NavbarDropdown className="dropdown navbar-nav nav-brand minute-clinic">



                            <NavItem>
                                <img src={navLogo(brandCode)} alt={altLogoTeladoc} className="header-logo" />
                            </NavItem>

                        </NavbarDropdown>

                        <div className="nav-actions">
                            <ul className="dropdown navbar-nav">
                                <LocaleContainer />
                                <li className="navigation-item--sub-action">
                                    <button onClick={this.displayHelp} aria-label="help" role="button">
                                        <span>
                                            <I18n scope="navigation_menu.middle-tier.help" text="label" />
                                        </span>
                                    </button>
                                </li>
                                <NavItem className="navigation-item--sub-action">
                                    <NavLink href="javascript:;"
                                        aria-label={translate(null, 'navigation_menu.middle-tier.logout', 'label')}
                                        onClick={this.confirmLogout}
                                    >
                                        <LogoutIcon width="17" height="17" />
                                        <span className="logout-text">
                                            <I18n scope="navigation_menu.middle-tier.logout" text="label" />
                                        </span>
                                    </NavLink>
                                </NavItem>
                            </ul>
                            <HelpModal active={showHelp} onExit={this.exitHelp} tollfreeNumber={tollfreeNumber} />
                            <ConfirmModal
                                active={showConfirmExit}
                                onConfirm={this.logout}
                                onCancel={this.cancelLogout}
                                confirmText={translate(null, 'navigation_menu.middle-tier.logout', 'confirm')}
                                cancelText={translate(null, 'navigation_menu.middle-tier.logout', 'cancel')}
                                confirmClass="button"
                                cancelClass="button cancel"
                                useChildren
                            >
                                <h3>
                                    <I18n scope="navigation_menu.messages" text="sign_out_message" />
                                </h3>
                            </ConfirmModal>
                        </div>
                        
                        <NavbarDropdown className="dropdown navbar-nav nav-brand minute-clinic logo-secondary">
                            
                            <NavItem>
                                <NavLink href={groupHomepageUrl} target="_blank" rel="noopener noreferrer">
                                    <img src={navLogo('topdanmark_secondary')} alt={altLogo} className="header-logo" />
                                </NavLink>
                            </NavItem>


                            
                        </NavbarDropdown>
                    </div>
                </div>
            </div>
        );
    }
}

MiddleTier.propTypes = {
    memberId: PropTypes.number.isRequired,
    groupHomepageUrl: PropTypes.string,
    tollfreeNumber: PropTypes.string
};

export { MiddleTier };
