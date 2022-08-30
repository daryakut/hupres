export type ImageProps = React.ImgHTMLAttributes<HTMLImageElement>;
export type Metadata = any;

export const Image: React.FC<ImageProps> = (props) => {
  return <img {...props} />;
};

interface LinkProps extends React.AnchorHTMLAttributes<HTMLAnchorElement> {}

export const Link: React.FC<LinkProps> = ({ children, ...props }) => {
  return (
    <a {...props}>
      {children}
    </a>
  );
};
