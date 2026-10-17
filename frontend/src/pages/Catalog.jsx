
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

      {/* K-Pop Groups */}
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

      {/* Selected Group's Idols */}
      {selectedGroup !== null && (
        <div>
          <h2>Idols</h2>

          <button onClick={() => setSelectedGroup(null)}>
            Hide Idols
          </button>

          <div className="catalog-grid">
            {filteredIdols.length > 0 ? (
              filteredIdols.map((idol) => (
                <div className="card" key={idol.id}>
                  <h3>{idol.name}</h3>

                  <p>
                    Group:{" "}
                    {
                      mockGroups.find(
                        (group) => group.id === idol.group
                      )?.name
                    }
                  </p>
                </div>
              ))
            ) : (
              <p>No idols available for this group.</p>
            )}
          </div>
        </div>
      )}
    </div>
  );
}

export default Catalog;
