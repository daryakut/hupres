import React from 'react';
import PropTypes from 'prop-types';
import TweenOne from 'rc-tween-one';
import ScrollOverPack from 'rc-scroll-anim/lib/ScrollOverPack';
import { Icon, Button } from 'antd';
import QueueAnim from 'rc-queue-anim';

export default function Page1({ isMobile }) {
  return (
    <ScrollOverPack id="page1" className="content-wrapper page">
      <QueueAnim
        type={isMobile ? 'bottom' : 'right'}
        className="text-wrapper"
        key="text1"
        leaveReverse
      >
        <hr key="hr" className="landing-hr"/>
        <h2 key="h2">ЩО ТАКЕ HUPRES</h2>
        <p key="p" style={{ maxWidth: 310 }}>近一年的中后台设计实践，积累了大量的优秀案例。</p>
        <div key="button">
          <a>
            <Button type="primary" size="large">
              了解更多
              <Icon type="right" />
            </Button>
          </a>
        </div>
      </QueueAnim>
      <QueueAnim
        type={isMobile ? 'bottom' : 'right'}
        className="text-wrapper"
        key="text2"
        leaveReverse
      >
        <hr key="hr" className="landing-hr"/>
        <h2 key="h2">ЩО ТАКЕ HUPRES</h2>
        <p key="p" style={{ maxWidth: 310 }}>近一年的中后台设计实践，积累了大量的优秀案例。</p>
        <div key="button">
          <a>
            <Button type="primary" size="large">
              了解更多
              <Icon type="right" />
            </Button>
          </a>
        </div>
      </QueueAnim>
    </ScrollOverPack>
  );
}
Page1.propTypes = {
  isMobile: PropTypes.bool,
};
