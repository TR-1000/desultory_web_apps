function UserList({ users, specialty }) {
  return (
    <div>
      <ul className="module quick-links">
        <li>
          <a href="ww.teladoc.com">Provider Resources</a>
        </li>

        {specialty === "General Medical" && (
          <li>
            <a href="www.teladoc.com">Covid-19 Guidelines</a>
          </li>
        )}
      </ul>

      <table>
        <thead>
          <tr>
            <th>Name</th>
            <th>Email</th>
          </tr>
        </thead>
        <tbody></tbody>
      </table>
    </div>
  );
}

export default UserList;
