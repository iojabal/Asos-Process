import { useState } from "react";

export default function OutputTable(){
    const [queue, setQueue] = useState(
        [
            [
                "B",
                "C",
                "D",
                "A",
                "E"
            ],
            [
                "C",
                "D",
                "A",
                "E"
            ],
            [
                "C",
                "D",
                "A",
                "E"
            ],
            [
                "D",
                "A",
                "E"
            ],
            [
                "D",
                "A",
                "E"
            ],
            [
                "A",
                "E"
            ],
            [
                "A",
                "E"
            ],
            [
                "E"
            ],
            [
                "E"
            ],
            [
                "E"
            ],
            [],
            []
        ]    
    )

    const [execution, setExecution] = useState( [
        0,
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
    ]
)

const maxLength = Math.max(...queue.map((datos) => (Array.isArray(datos) ? datos.length : 1)));

// Crea un nuevo arreglo transpuesto
const transposedQueue = Array.from({ length: maxLength }, (_, colIndex) =>
  queue.map((datos) => (datos[colIndex]))
);

    return(
        <div>
            <table className="">
                <tr>
                    {execution.map((executionData,rowIndex) => (
                        <td key={rowIndex} className="p-3 border border-black">
                                {executionData}
                        </td>
                    ))}
                </tr>
            </table>

            <table>
                {transposedQueue.map((column, colIndex) => (
                <tr key={colIndex} className=" ">
                    {column.map((proc, rowIndex) => (
                    <td key={rowIndex} className=" p-3 border border-black">{proc}</td>
                    ))}
                </tr>
                ))}
            </table>
        </div>
    );
}