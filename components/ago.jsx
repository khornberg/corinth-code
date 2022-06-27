export default function Ago({ text, timeInThePast, current }) {
  const relativeTime = new Intl.RelativeTimeFormat("en", { style: "long" });
  const date = Date.parse(
    `${current.getFullYear()}-${current.getMonth() + 1}-${current.getDate()}`
  );
  const dateDiff = Math.round(
    (date - Date.parse(timeInThePast)) / (1000 * 86400 * -1)
  );
  return (
    <p>
      <span className="text-gray">
        {text} <time>{relativeTime.format(dateDiff, "day")}</time>
      </span>
    </p>
  );
}
