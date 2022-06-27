export default function Column({ children, position }) {
  const positions = {
    centered: "col-4 col-mx-auto",
  };
  const className = `column ${positions[position]}`;
  return <div className={className}>{children}</div>;
}
