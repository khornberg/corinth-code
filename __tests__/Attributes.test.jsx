import { expect, test, afterEach } from "vitest";
import { render, screen, cleanup } from "@testing-library/react";
import Attributes from "../components/attributes";

afterEach(cleanup);

test("attributes compoment", () => {
  const obj = { a: "foo", b: "bar" };
  const mapping = { a: "First", b: "B" };
  render(<Attributes obj={obj} mapping={mapping} />);
  const a = screen.getByText("First: foo");
  const b = screen.getByText("B: bar");
  expect(a.innerHTML).toBe("First: foo");
  expect(b.innerHTML).toBe("B: bar");
});
