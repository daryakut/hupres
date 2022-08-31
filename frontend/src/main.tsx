import './main.css';
// import './tailwind.css';

import Application2 from "./Application2";
import React from 'react';
import { createRoot } from 'react-dom/client';
// import Application from './Application';

// Say something
console.log('[ERWT] : Renderer execution started');

// Application to Render
// const app = <Application />;
const app = <Application2 />;

// Render application in DOM
createRoot(document.getElementById('app')).render(app);
