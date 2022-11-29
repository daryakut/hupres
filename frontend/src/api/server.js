let baseUrl = undefined;

const updateBaseUrl = () => {
  if (process.env.HUPRES_ENV === 'production') {
    console.log('Connecting to production server')
    baseUrl = `${process.env.HUPRES_PROD_HOSTNAME}:${process.env.HUPRES_APP_PORT}`
    // 'https://hupres-backend.onrender.com'
  } else if (process.env.HUPRES_ENV === 'development_docker') {
    console.log('Connecting to development_docker server')
    baseUrl = `http://localhost:${process.env.HUPRES_APP_PORT}`
  } else {
    console.log('Connecting to local server')
    // when running in development mode without docker, the backend is running on port 8000
    baseUrl = 'http://localhost:8000';
  }
  console.log(`Connecting to server in ${process.env.HUPRES_ENV} environment on ${baseUrl}`)
  return baseUrl;
}

// Lazy initialization of baseUrl in case environment variables aren't available at startup.
// TODO: remove this as I think they should be
export const getBaseUrl = () => {
  if (!baseUrl) {
    updateBaseUrl();
  }
  return baseUrl;
}
