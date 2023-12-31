import React, { useState } from 'react';

export default function Tabla(props) {
  const [data, setData] = useState(
    new Array(props.numeroFilas).fill({
      process: '',
      cputime: '',
      priority: '',
      arrivedTime: ''
    })
  );

  const handleInputChange = (e, rowIndex, colName) => {
    const updatedData = [...data];
    updatedData[rowIndex] = {
      ...updatedData[rowIndex],
      [colName]: e.target.value
    };
    setData(updatedData);
  };

  const enviarDatos = (e) => {
    e.preventDefault()
    fetch("http://127.0.0.1:5000/" + props.proceso, {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(data)
    })
      .then((response) => {
        if (!response.ok) {
          throw new Error("la Respuesta del Servidor Fue: " + response.status)
        }
        return response.json()
      }).then((mdg) => {
        console.log(mdg)
        // proceso.
      })
    console.log(props.proceso)
    console.log(data)
  };

  return (
    <div className='p-5 flex justify-center'>
      <form onSubmit={enviarDatos}>
        <div className=' max-w-7xl'>
          <table className="border-collapse border border-black mb-4 w-full">
            <thead className='border border-black'>
              <tr className='text-xs md:text-xl'>
                <th className="border border-black p-2 bg-yellow-800 text-white">PROCESO</th>
                {props.tee === true && <th className="border border-black p-2 bg-yellow-700 text-white">TIEMPO DE EJECUCIÓN</th>}
                {props.tll === true && <th className="border border-black p-2 bg-yellow-600 text-white">TIEMPO DE LLEGADA</th>}
                {props.prio === true && <th className="border border-black p-2 bg-yellow-500 text-white">PRIORIDAD</th>}
              </tr>
            </thead>
            <tbody>
              {data.map((rowData, rowIndex) => (
                <tr key={rowIndex}>
                  <td className="border border-black">
                    <input
                      type="text"
                      className=' w-full text-center'
                      value={rowData.proceso}
                      onChange={(e) => handleInputChange(e, rowIndex, 'process')}
                      required
                    />
                  </td>
                  {props.tee === true &&
                    <td className="border border-black">
                      <input
                        type="number"
                        className=' w-full text-center'
                        value={rowData.tiempoEjecucion}
                        onChange={(e) => handleInputChange(e, rowIndex, 'cputime')}
                        min={1}
                        required
                      />
                    </td>
                  }
                  {props.tll === true &&
                    <td className="border border-black">
                      <input
                        type="number"
                        className=' w-full text-center'
                        value={rowData.tiempoLlegada}
                        onChange={(e) => handleInputChange(e, rowIndex, 'arrivedTime')}
                        min={1}
                        required
                      />
                    </td>
                  }
                  {props.prio === true &&
                    <td className="border border-black">
                      <input
                        type="number"
                        className=' w-full text-center'
                        value={rowData.prioridad}
                        onChange={(e) => handleInputChange(e, rowIndex, 'priority')}
                        min={1}
                        required
                      />
                    </td>
                  }
                </tr>
              ))}
            </tbody>
          </table>

          <div className=' flex justify-end w-full'>
            <button type='Submit' className='p-3 hover:bg-yellow-800 bg-yellow-950 text-white'> ACEPTAR</button>
          </div>
        </div>
      </form>
    </div>
  );
}
