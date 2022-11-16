import React from 'react';
import classNames from 'classnames';
import {Dropdown, Icon, Menu} from 'antd';
import {UserOutlined} from '@ant-design/icons';
import {Link, useHistory} from "react-router-dom";
import {getBaseUrl} from "../api/server";
import {useUser} from "../User/UserProvider";
import {getCurrentUser, logout} from "../api/users_api";
import {useMediaQuery} from "react-responsive";
import {motion} from 'framer-motion';

const searchEngine = 'Google';

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
    transition: {duration: 0.5}
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
        {/*<Menu.Item>*/}
        {/*  <Link key="button" to="/quiz">ПРОФІЛЬ</Link>*/}
        {/*</Menu.Item>*/}
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

  const isMobile = useMediaQuery({query: '(max-width: 768px)'})
  const menuMode = isMobile ? 'inline' : 'horizontal';

  const isLandingPage = window.location.pathname === '/';

  const headerClassName = classNames({
    'home-nav-main': true,
    'home-nav-black': !isLandingPage,
  });

  const menuClassName = classNames({
    'main-menu': true,
    'main-menu-mobile': isMobile,
  });

  const menu = (
    <Menu className={menuClassName} mode={menuMode} defaultSelectedKeys={['home']} id="nav" key="nav">
      <Menu.Item key="home">
        ЩО ТАКЕ HUPRES
      </Menu.Item>
      <Menu.Item key="docs/spec">
        ПРАКТИЧНЕ ВИКОРИСТАННЯ
      </Menu.Item>
      <Menu.Item key="docs/pattern">
        ПРОДУКТИ
      </Menu.Item>
      <Menu.Item key="docs/react">
        СТРАТЕГІЯ РОЗВИТКУ
      </Menu.Item>
    </Menu>
  );

  return (
    <>
      <header id="header" className={headerClassName}>
        {/*{mobileMenuVisible ? (*/}
        {/*  <div className="menu-mobile-drawn">*/}
        {/*    <div key="home" className="menu-mobile-drawn-item">*/}
        {/*      ЩО ТАКЕ HUPRES*/}
        {/*    </div>*/}
        {/*    <div key="docs/spec" className="menu-mobile-drawn-item">*/}
        {/*      ПРАКТИЧНЕ ВИКОРИСТАННЯ*/}
        {/*    </div>*/}
        {/*    <div key="docs/pattern" className="menu-mobile-drawn-item">*/}
        {/*      ПРОДУКТИ*/}
        {/*    </div>*/}
        {/*    <div key="docs/react" className="menu-mobile-drawn-item">*/}
        {/*      СТРАТЕГІЯ РОЗВИТКУ*/}
        {/*    </div>*/}
        {/*  </div>*/}
        {/*) : null}*/}
        {/*<Col lg={4} md={5} sm={22} xs={22}>*/}
        {/*      <TweenOne*/}
        {/*        animation={{*/}
        {/*          x: 80,*/}
        {/*          scale: 0.5,*/}
        {/*          rotate: 120,*/}
        {/*          yoyo: true, // demo 演示需要*/}
        {/*          repeat: -1, // demo 演示需要*/}
        {/*          duration: 1000*/}
        {/*        }}*/}
        {/*        paused={props.paused}*/}
        {/*        style={{ transform: 'translateX(-80px)' }}*/}
        {/*        className="code-box-shape"*/}
        {/*      />*/}
        <div className="home-nav-logo">
          <a id="logo" href='/'>
            <img alt="logo" src="https://hupres.com/image/catalog/logo.svg"/>
          </a>
        </div>
        {/*<Col lg={18} md={17} sm={0} xs={0}>*/}
        {/*{!isMobile ? (*/}
        {isMobile ? (
          <>
            {/*<motion.div*/}
            {/*  initial="hidden"*/}
            {/*  animate={mobileMenuVisible ? "visible" : "hidden"}*/}
            {/*  variants={menuVariants}*/}
            {/*>*/}
              {/*{menu}*/}
            {mobileMenuVisible ? (
              <div className="menu-mobile-drawn">
                <div key="home" className="menu-mobile-drawn-item">
                  ЩО ТАКЕ HUPRES
                </div>
                <div key="docs/spec" className="menu-mobile-drawn-item">
                  ПРАКТИЧНЕ ВИКОРИСТАННЯ
                </div>
                <div key="docs/pattern" className="menu-mobile-drawn-item">
                  ПРОДУКТИ
                </div>
                <div key="docs/react" className="menu-mobile-drawn-item">
                  СТРАТЕГІЯ РОЗВИТКУ
                </div>
              </div>
              ) : null}
            {/*</motion.div>*/}
            <Icon
              className="nav-phone-icon"
              type="menu"
              onClick={() => setMobileMenuVisible(!mobileMenuVisible)}
            />
          </>
        ) : (
          <>
            {menu}
            <div className="home-nav-profile">
              {/*<UserOutlined key="profile" style={{ fontSize: '26px', color: '#ddd', margin: 25, cursor: "pointer" }}/>*/}
              <SigninDropdown/>
            </div>
          </>
        )}
        {/*) : null}*/}
      </header>
      {!isLandingPage ? (
        <div style={{height: 80}}/>
      ) : null}
    </>
  );
}

export default Header;
