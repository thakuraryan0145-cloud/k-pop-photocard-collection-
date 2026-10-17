
import { useState } from "react";
import { mockGroups, mockIdols } from "../data/mockData";

function Catalog() {
  const [selectedGroup, setSelectedGroup] = useState(null);

  const filteredIdols = mockIdols.filter(
    (idol) => idol.group === selectedGroup
  );

  return (
    <div className="page">
      <h1>Photocard Catalog</h1>
      <p>Explore K-Pop photocards.</p>

      <div className="catalog-grid">
        {mockGroups.map((group) => (
          <div className="card" key={group.id}>
            <h2>{group.name}</h2>
            <p>Photocard collection</p>

            <button onClick={() => setSelectedGroup(group.id)}>
              View Idols
            </button>
          </div>
        ))}
      </div>

      {selectedGroup !== null && (
        <div>
          <h2>Idols</h2>

          {filteredIdols.length > 0 ? (
            filteredIdols.map((idol) => (
              <div className="card" key={idol.id}>
                <h3>{idol.name}</h3>
              </div>
            ))
          ) : (
            <p>No idols available for this group.</p>
          )}
        </div>
      )}
    </div>
  );
}

export default Catalog;
