import { companySection, creadores } from "../constants";

const FooterContent = ({ className = '', section, name }) => {
    return (
        <div className={`flex items-center ${className}`}>
            <div className='footer-content'>
                <h4 className='text-white mb-2 text-lg'>{name}</h4>
                {
                    section.map((i, index) => (
                        <li className='text-white text-base block' key={index}>
                            <img src="/bailarina.gif" alt="" className="w-10 h-10 inline-block mr-2" />
                            <a href="#" className="text-white">
                                {i}
                            </a>
                        </li>
                    ))
                }
            </div>
        </div>
    );
};

const Creators = ({ className = '', section, name }) => {
    return (
        <div className={`flex items-center ${className}`}>
            <div className='footer-content'>
                <h4 className='text-white mb-2 text-lg'>{name}</h4>
                {
                    section.map((item, index) => (
                        <li className='text-white text-base block' key={index}>
                            <img src={item.foto} alt={item.name} className="w-20 h-20 inline-block mr-2" />
                            <span className="text-white">{item.name}</span>
                            <span className="text-neutral-950 ml-2">({item.ocupacion})</span>
                        </li>
                    ))
                }
            </div>
        </div>
    );
};

export const Footer = () => {
    return (
        <section className="bg-black text-white p-5">
            <div className="container grid grid-cols-2 md:grid-cols-4 gap-5">
                <div className="flex flex-col justify-start items-center">
                    <a href="#" className="text-2xl font-bold">Cola d<span className="text-green-500">e Procesos</span></a>
                    <p className="text-base m-2 leading-6">
                        Lorem ipsum dolor sit amet, consectetur adipisicing elit. adsfdafdsafdsafdsagfahfdfafas
                    </p>
                    <img src="/bailarina2.gif" alt="" className="w-1/2 h-1/2 inline-block mr-2" />
                    <div className="flex gap-2">
                        <a href="#" className="text-2xl"><i className="bx bxl-tiktok"></i></a>
                        <a href="#" className="text-2xl"><i className="bx bxl-instagram-alt"></i></a>
                    </div>
                </div>

                <FooterContent section={companySection} name="test" />

                <img src="/calacahd.jpg" className="w-64 h-64 inline-block mr-2" />

                <Creators section={creadores} name="Desarrolladores" />

            </div>
        </section >
    );
};
