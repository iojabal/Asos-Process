import { useState } from "react";

export default function OutputTable() {
  const [queue, setQueue] = useState([
    ["B", "C", "D", "A", "E"],
    ["C", "D", "A", "E"],
    ["C", "D", "A", "E"],
    ["D", "A", "E"],
    ["D", "A", "E"],
    ["A", "E"],
    ["A", "E"],
    ["E"],
    ["E"],
    ["E"],
    [],
    []
  ]);

  const [execution, setExecution] = useState([
    "Ø",
    "B",
    "B",
    "C",
    "C",
    "D",
    "D",
    "A",
    "A",
    "A",
    "E",
    "E",
    "E"
  ]);

  // Eliminar arreglos vacíos
  const filteredQueue = queue.filter((datos) => datos.length > 0);

  // Obtén la longitud de la fila más larga en el arreglo filtrado
  const maxLength = Math.max(...filteredQueue.map((datos) => datos.length));

  // Crea un nuevo arreglo transpuesto
  const transposedQueue = Array.from({ length: maxLength }, (_, colIndex) =>
    filteredQueue.map((datos) => datos[colIndex])
  );

  return (
    <div>
      <div className="p-2">
        <table className="">
          <tr>
            {execution.map((executionData, rowIndex) => (
              <td key={rowIndex} className="p-3 border border-black">
                {executionData}
              </td>
            ))}
          </tr>
        </table>
      </div>

      <div className="p-2">
        <table>
          {transposedQueue.map((column, colIndex) => (
            <tr key={colIndex} className=" ">
              {column.map((proc, rowIndex) => (
                <td key={rowIndex} className="p-3 border border-black">
                  {proc}
                </td>
              ))}
            </tr>
          ))}
        </table>
      </div>
    </div>
  );
}
