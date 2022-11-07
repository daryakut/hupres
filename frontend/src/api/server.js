export const getBaseUrl = () => {
  console.log(`Connecting to server in ${process.env.NODE_ENV} environment`)
  return process.env.NODE_ENV === 'production' ? 'https://hupres-backend.onrender.com' : 'http://localhost:8000';
}
