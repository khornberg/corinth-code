export default function Attributes({ obj, mapping }) {
  const attributes = Object.keys(mapping).map((n) => (
    <li key={n}>
      {mapping[n]}: {obj[n]}
    </li>
  ));
  return <>{attributes}</>;
}
