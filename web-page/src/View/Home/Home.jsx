import Table from '../../components/InputTable/InputTable.jsx'
import { useState } from 'react';

export default function Home(){
    const [proceso, setProceso] = useState('')
    const [cambioContexto, setCambioContexto] = useState(false);
    
    const onChangeValue = (event) => {
        setProceso(event.target.value)
        console.log(event.target.value);
    };

    const handleCambioContextoChange = (event) => {
        console.log(event.target.checked)
        setCambioContexto(event.target.checked);
      };

    return(
        <>
            <div className='flex flex-col sm:flex-row justify-center'>
                <div className='flex flex-col p-5'>
                    <h2>SELECCIONE MÉTODO A RESOLVER:</h2>
                    <div className='flex flex-col justify-between max-w-lg p-4' onChange={onChangeValue}>
                        <div className='flex p-2'><input type='radio' name='Metodo' value='priority'/>PRIORIDAD </div>
                        <div className='flex p-2'><input type='radio' name='Metodo' value='FCFS'/>FCFS</div>
                        <div className='flex p-2'><input type='radio' name='Metodo' value='SRT'/>SRT</div>
                        <div className='flex p-2'><input type='radio' name='Metodo' value='SJF'/>SJF</div>
                        <div className='flex p-2'><input type='radio' name='Metodo' value='rr'/>ROUND ROBIN</div> 
                    </div>
                </div>

                <div className=' flex md:flex-col justify-center px-5 space-x-3 items-center'>
                    <label className='md:p-4'> INGRESE EL NUMERO DE PROCESOS:</label>
                    <input
                        type='number'
                        className=' border border-black text-center'
                    />
                </div>

                <div className='flex flex-col justify-center'>
                    <div className=' flex flex-row p-5 space-x-3 items-center'>
                        <label>¿CAMBIO DE CONTEXTO? </label>
                        <input 
                            type='checkbox'
                            checked = {cambioContexto}
                            onChange={handleCambioContextoChange}
                            className='border border-black' 
                            name='CContexto'></input>
                    </div>
                    {cambioContexto && (
                        <div className='px-4'>
                            <input
                            className='border border-black text-center'
                            type='number'
                            />
                        </div>
                    )}
                </div>
            </div>

            {proceso === 'priority' && <Table numeroFilas = {5} proceso={proceso} tll={false} prio ={true} tee={true}></Table>}
            {proceso === 'FCFS' && <Table numeroFilas = {5} proceso={proceso} tll={true} prio ={false} tee={true}></Table>}
            {proceso === 'SRT' && <Table numeroFilas = {5} proceso={proceso} tll={true} prio ={false} tee={true}></Table>}
            {proceso === 'SJF' && <Table numeroFilas = {5} proceso={proceso} tll={true} prio ={false} tee={true}></Table>}
            {proceso === 'rr' && <Table numeroFilas = {5} proceso={proceso} tll={false} prio ={false} tee={true}></Table>}
        </>
    );
}