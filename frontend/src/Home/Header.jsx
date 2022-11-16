import React from 'react';
import classNames from 'classnames';
import {Dropdown, Menu} from 'antd';
import {UserOutlined} from '@ant-design/icons';
import {Link, useHistory} from "react-router-dom";
import {getBaseUrl} from "../api/server";
import {useUser} from "../User/UserProvider";
import {getCurrentUser, logout} from "../api/users_api";
import {useMediaQuery} from "react-responsive";

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
  const isMobile = useMediaQuery({ query: '(max-width: 768px)' })
  const menuMode = isMobile ? 'inline' : 'horizontal';

  const isLandingPage = window.location.pathname === '/';

  const headerClassName = classNames({
    'home-nav-main': true,
    'home-nav-black': !isLandingPage,
  });

  const menu = [
    // <Button className="header-lang-button" ghost size="small" key="lang">
    //   English
    // </Button>,
    <Menu mode={menuMode} defaultSelectedKeys={['home']} id="nav" key="nav">
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
    </Menu>,
  ];

  return (
    <>
      <header id="header" className={headerClassName}>
        {/*{menuMode === 'inline' ? (*/}
        {/*  <Popover*/}
        {/*    overlayClassName="popover-menu"*/}
        {/*    placement="bottomRight"*/}
        {/*    content={menu}*/}
        {/*    trigger="click"*/}
        {/*    visible={menuVisible}*/}
        {/*    arrowPointAtCenter*/}
        {/*    onVisibleChange={this.onMenuVisibleChange}*/}
        {/*  >*/}
        {/*    <Icon*/}
        {/*      className="nav-phone-icon"*/}
        {/*      type="menu"*/}
        {/*      onClick={this.handleShowMenu}*/}
        {/*    />*/}
        {/*  </Popover>*/}
        {/*) : null}*/}
        {/*<Col lg={4} md={5} sm={22} xs={22}>*/}
        <div className="home-nav-logo">
          <a id="logo" href='/'>
            <img alt="logo" src="https://hupres.com/image/catalog/logo.svg"/>
          </a>
        </div>
        {/*<Col lg={18} md={17} sm={0} xs={0}>*/}
        {/*  {menuMode === 'horizontal' ? menu : null}*/}
        {/*</Col>*/}
        {/*<Col lg={2} md={2} sm={2} xs={2}>*/}
        <div className="home-nav-profile">
          {/*<UserOutlined key="profile" style={{ fontSize: '26px', color: '#ddd', margin: 25, cursor: "pointer" }}/>*/}
          <SigninDropdown/>
        </div>
      </header>
      {!isLandingPage ? (
        <div style={{height: 80}}/>
      ) : null}
    </>
  );
}

export default Header;
