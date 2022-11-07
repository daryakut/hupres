import React from 'react';
import PropTypes from 'prop-types';
import classNames from 'classnames';
import {Col, Dropdown, Icon, Menu, Popover, Row} from 'antd';
import {UserOutlined} from '@ant-design/icons';
import {Link} from "react-router-dom";

const searchEngine = 'Google';

const menu = (
  <Menu>
    <Menu.Item>
      <Link to="/login">РЕЄСТРАЦІЯ</Link>
    </Menu.Item>
    <Menu.Item>
      <Link to="/login">АВТОРИЗАЦІЯ</Link>
    </Menu.Item>
  </Menu>
);

const SigninDropdown = () => (
  <Dropdown overlay={menu} placement="bottomRight">
    <UserOutlined key="profile" style={{fontSize: '26px', color: '#ddd', margin: '25px', cursor: 'pointer'}}/>
  </Dropdown>
);

export default class Header extends React.Component {
  static propTypes = {
    isFirstScreen: PropTypes.bool,
    isMoblie: PropTypes.bool,
  }
  state = {
    menuVisible: false,
  };
  onMenuVisibleChange = (visible) => {
    this.setState({
      menuVisible: visible,
    });
  }
  handleShowMenu = () => {
    this.setState({
      menuVisible: true,
    });
  }

  handleHideMenu = () => {
    this.setState({
      menuVisible: false,
    });
  }

  handleSelectFilter = (value, option) => {
    const optionValue = option.props['data-label'];
    return optionValue === searchEngine ||
      optionValue.indexOf(value.toLowerCase()) > -1;
  }

  render() {
    const {isFirstScreen, isMoblie} = this.props;
    const {menuVisible} = this.state;
    const menuMode = isMoblie ? 'inline' : 'horizontal';
    const headerClassName = classNames({
      clearfix: true,
      'home-nav-white': !isFirstScreen,
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
      <header id="header" className={headerClassName}>
        {menuMode === 'inline' ? (
          <Popover
            overlayClassName="popover-menu"
            placement="bottomRight"
            content={menu}
            trigger="click"
            visible={menuVisible}
            arrowPointAtCenter
            onVisibleChange={this.onMenuVisibleChange}
          >
            <Icon
              className="nav-phone-icon"
              type="menu"
              onClick={this.handleShowMenu}
            />
          </Popover>
        ) : null}
        <Row>
          <Col lg={4} md={5} sm={22} xs={22}>
            <a id="logo">
              <img alt="logo" src="https://hupres.com/image/catalog/logo.svg"/>
            </a>
          </Col>
          <Col lg={18} md={17} sm={0} xs={0}>
            {menuMode === 'horizontal' ? menu : null}
          </Col>
          <Col lg={2} md={2} sm={2} xs={2}>
            {/*<UserOutlined key="profile" style={{ fontSize: '26px', color: '#ddd', margin: 25, cursor: "pointer" }}/>*/}
            <SigninDropdown/>
          </Col>
        </Row>
      </header>
    );
  }
}
