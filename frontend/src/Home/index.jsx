import React, {useEffect} from 'react';
import DocumentTitle from 'react-document-title';
import Header from './Header';
import Banner from './Banner';
import './static/style';
import PracticalApplication from "./PracticalApplication";
import HowItWorks from "./HowItWorks";
import Qualities from "./Qualities";


const Home = () => {

  useEffect(() => {
    const redirectUrl = localStorage.getItem('redirectUrl');
    if (redirectUrl) {
      localStorage.removeItem('redirectUrl');
      window.location.href = redirectUrl;
    }
  }, []);

  const onEnterChange = (e) => {
    console.log("Scrolling!", e)
  }

  return (
    [
      <Header key="header"/>,
      <Banner key="banner" onEnterChange={onEnterChange}/>,
      <PracticalApplication key="page1" isMobile={false} />,
      <Qualities key="page3" isMobile={false} />,
      <HowItWorks key="page2" isMobile={false} />,
      // <Page2 key="page2" />,
      // <Page3 key="page3" isMobile={this.state.isMobile} />,
      // <Page4 key="page4" />,
      // <Footer key="footer" />,
      <DocumentTitle title="Hupres.com - психологічний портрет кожної людини" key="title"/>,
    ]
  );
}
export default Home;
