export const getBaseUrl = () => {
  let baseUrl;
  if (process.env.HUPRES_ENV === 'production') {
    baseUrl = `${process.env.HUPRES_PROD_HOSTNAME}:${process.env.HUPRES_APP_PORT}`
    // 'https://hupres-backend.onrender.com'
  } else if (process.env.HUPRES_ENV === 'development_docker') {
    baseUrl = `http://localhost:${process.env.HUPRES_APP_PORT}`
  } else {
    // when running in development mode without docker, the backend is running on port 8000
    baseUrl = 'http://localhost:8000';
  }
  console.log(`Connecting to server in ${process.env.HUPRES_ENV} environment on ${baseUrl}`)
  return baseUrl;
}
