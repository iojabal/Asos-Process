import Table from '../../components/InputTable/InputTable.jsx'

// PRIORIDAD MENOS TIEMPO DE LLEGADA
// FCFS MENOS PRIORIDAD
// SJF SOLO TIEMPO DE CPU
// SRT SIN PRIORIDAD
// RR SOLO TIEMPO DE CPU

export default function Home(){
    var proceso = ''
    const onChangeValue = (event) => {
        proceso = event.target.value
        console.log(event.target.value);
    };

    return(
        <>
            <div className='flex flex-col'>
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

                <div className=' flex flex-row p-5'>
                    <label> INGRESE EL NUMERO DE PROCESOS:</label>
                    <input
                        type='number'
                        className=' border border-black text-center'
                    />
                </div>
            </div>
        
            <Table numeroFilas = {5} proceso={proceso}></Table>
        </>
    );
}