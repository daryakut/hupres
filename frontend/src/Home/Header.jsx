import React, {useEffect} from 'react';
import classNames from 'classnames';
import {Dropdown, Menu} from 'antd';
import {MenuOutlined, UserOutlined} from '@ant-design/icons';
import {Link, useHistory} from "react-router-dom";
import {getBaseUrl} from "../api/server";
import {useUser} from "../User/UserProvider";
import {getCurrentUser, logout} from "../api/users_api";
import {useMediaQuery} from "react-responsive";
import {motion} from 'framer-motion';
import {Link as ScrollLink, scroller} from 'react-scroll';

const LinkOrScrollLink = (props) => {
  const isLandingPage = window.location.pathname === '/';

  const {
    to,
    smooth,
    duration,
    ...rest
  } = props;

  return isLandingPage ? (
    <ScrollLink to={to} smooth={smooth} duration={duration} {...rest} />
  ) : (
    <a href={`/#${to}`} {...rest} />
  )
}

const loggedOutMenu = (
  <Menu>
    <Menu.Item>
      <a href={`${getBaseUrl()}/api/users/google-login`}>РЕЄСТРАЦІЯ</a>
    </Menu.Item>
    <Menu.Item>
      <a href={`${getBaseUrl()}/api/users/google-login`}>УВІЙТИ</a>
    </Menu.Item>
  </Menu>
);

const menuVariants = {
  hidden: {
    y: '-100%',
    opacity: 0
  },
  visible: {
    y: 0,
    opacity: 1,
    transition: {duration: 0.3}
  }
};

const SigninDropdown = () => {
  const {user, setUser} = useUser();
  let history = useHistory();

  const logoutAndRedirect = async () => {
    await logout();
    const user = await getCurrentUser();
    setUser(user)
    history.push('/')
  }

  let menu = loggedOutMenu;
  if (user) {
    menu = (
      <Menu>
        <Menu.Item>
          <Link key="button" to="/quizzes">МОЇ АНКЕТИ</Link>
        </Menu.Item>
        <Menu.Item>
          <a onClick={logoutAndRedirect}>ВИЙТИ</a>
        </Menu.Item>
      </Menu>
    );
  }

  const userName = user ? user.email_address.split("@")[0] : '';
  return (
    <Dropdown overlay={menu} placement="bottomRight">
      <div className="user-profile-dropdown">
        <div className="user-profile">{userName}</div>
        <UserOutlined key="profile" style={{fontSize: '26px', color: '#ddd'}}/>
      </div>
    </Dropdown>
  );
};

const Header = () => {
  const [mobileMenuVisible, setMobileMenuVisible] = React.useState(false);
  const {user, setUser} = useUser();
  let history = useHistory();
  const isLoggedIn = !!user;

  // TODO: duplicate logoutAndRedirect, refactor
  const logoutAndRedirect = async () => {
    await logout();
    const user = await getCurrentUser();
    setUser(user)
    history.push('/')
  }

  const isMobile = useMediaQuery({query: '(max-width: 992px)'})

  const isLandingPageOrDisclaimer = window.location.pathname === '/'
    || window.location.pathname === '/disclaimer';

  const headerClassName = classNames({
    'home-nav-main': true,
    'home-nav-black': !isLandingPageOrDisclaimer,
  });

  return (
    <>
      <header id="header" className={headerClassName}>
        <div className="home-nav-logo">
          <a className="main-logo" href='/'>
            <img alt="logo" src="https://hupres.com/image/catalog/logo.svg"/>
          </a>
        </div>
        {isMobile ? (
          <>
            <motion.div
              className="menu-mobile-drawn-container"
              initial="hidden"
              animate={mobileMenuVisible ? "visible" : "hidden"}
              variants={menuVariants}
            >
              <div className="menu-mobile-drawn">
                {isLandingPageOrDisclaimer ? (
                  <>
                    <LinkOrScrollLink
                      to="practice-page"
                      smooth={true}
                      duration={300}
                      className="menu-mobile-drawn-item"
                      onClick={() => setMobileMenuVisible(false)}
                    >
                      ПРАКТИЧНЕ ЗАСТОСУВАННЯ
                    </LinkOrScrollLink>
                    <LinkOrScrollLink
                      to="how-it-works-page"
                      smooth={true}
                      duration={600}
                      className="menu-mobile-drawn-item"
                      onClick={() => setMobileMenuVisible(false)}
                    >
                      ЯК ЦЕ ПРАЦЮЄ
                    </LinkOrScrollLink>
                    <LinkOrScrollLink
                      to="future-page"
                      smooth={true}
                      duration={900}
                      className="menu-mobile-drawn-item"
                      onClick={() => setMobileMenuVisible(false)}
                    >
                      МАЙБУТНЄ
                    </LinkOrScrollLink>
                  </>
                ) : null}
                {isMobile ? (
                  <>
                    {isLoggedIn ? (
                      <>
                        <Link className="menu-mobile-drawn-item" key="button" to="/quizzes">МОЇ АНКЕТИ</Link>
                        <a className="menu-mobile-drawn-item" onClick={logoutAndRedirect}>ВИЙТИ</a>
                      </>
                    ) : (
                      <>
                        <a className="menu-mobile-drawn-item"
                           href={`${getBaseUrl()}/api/users/google-login`}>
                          <UserOutlined style={{fontSize: '26px', marginRight: 10, color: '#ddd'}}/>
                          РЕЄСТРАЦІЯ
                        </a>
                        <a className="menu-mobile-drawn-item"
                           href={`${getBaseUrl()}/api/users/google-login`}>
                          <UserOutlined style={{fontSize: '26px', marginRight: 10, color: '#ddd'}}/>
                          УВІЙТИ
                        </a>
                      </>
                    )}
                  </>
                ) : null}
              </div>
            </motion.div>
            <MenuOutlined
              className="mobile-menu-show-icon"
              onClick={() => setMobileMenuVisible(!mobileMenuVisible)}
            />
          </>
        ) : (
          <>
            {isLandingPageOrDisclaimer ? (
              <div className="custom-menu">
                <LinkOrScrollLink to="practice-page" smooth={true} duration={300} key="practice" className="menu-item">
                  ПРАКТИЧНЕ ЗАСТОСУВАННЯ
                </LinkOrScrollLink>
                <LinkOrScrollLink to="how-it-works-page" smooth={true} duration={600} key="how-it-works"
                                  className="menu-item">
                  ЯК ЦЕ ПРАЦЮЄ
                </LinkOrScrollLink>
                <LinkOrScrollLink to="future-page" smooth={true} duration={900} key="future" className="menu-item">
                  МАЙБУТНЄ
                </LinkOrScrollLink>
              </div>
            ) : null}
            <div className="home-nav-profile">
              <SigninDropdown/>
            </div>
          </>
        )}
      </header>
      {!isLandingPageOrDisclaimer ? (
        <div style={{height: 80}}/>
      ) : null}
    </>
  );
}

export default Header;
