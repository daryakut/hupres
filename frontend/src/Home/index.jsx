import React, {useEffect} from 'react';
import DocumentTitle from 'react-document-title';
import Header from './Header';
import Banner from './Banner';
import './static/style';
import PracticePage from "./PracticePage";
import HowItWorksPage from "./HowItWorksPage";
import QualitiesPage from "./QualitiesPage";
import FuturePage from "./FuturePage";
import {Link as ScrollLink, scroller} from 'react-scroll';


const Home = () => {

  useEffect(() => {
    const redirectUrl = localStorage.getItem('redirectUrl');
    if (redirectUrl) {
      localStorage.removeItem('redirectUrl');
      window.location.href = redirectUrl;
    }

    // TODO: Fix this as it jumps back to the top after the page loads, maybe use HashRouter
    if (window.location.hash && window.location.hash.length > 1) {
      const elementId = window.location.hash.substring(1); // Removes the first two characters '/#'
      console.log("NAVIGATING", elementId)
      scroller.scrollTo(elementId, {
        duration: 300,
        delay: 0,
        smooth: 'easeInOutQuart'
      });
      window.location.hash = '';
    }
  }, [])


  const onEnterChange = (e) => {
    console.log("Scrolling!", e)
  }

  return (
    [
      <Header key="header"/>,
      <Banner key="banner" onEnterChange={onEnterChange}/>,
      <PracticePage key="page1"/>,
      <QualitiesPage key="page3"/>,
      <HowItWorksPage key="page2"/>,
      <FuturePage key="page4"/>,
      // <Page2 key="page2" />,
      // <Page3 key="page3" isMobile={this.state.isMobile} />,
      // <Page4 key="page4" />,
      // <Footer key="footer" />,
      <DocumentTitle title="Hupres.com - психологічний портрет кожної людини" key="title"/>,
    ]
  );
}
export default Home;
