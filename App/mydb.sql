SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `mydb`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `antecedentesfamiliares`
--

CREATE TABLE `antecedentesfamiliares` (
  `idantecentesFamiliares` int(11) NOT NULL,
  `mapaAntecedentesFamiliares` binary(25) DEFAULT NULL,
  `Paciente_expediente` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `antecedentespersonales`
--

CREATE TABLE `antecedentespersonales` (
  `idantecedentesPersonales` int(11) NOT NULL,
  `cardiovascular` varchar(45) DEFAULT NULL,
  `hta` varchar(45) DEFAULT NULL,
  `tabaquismo` tinyint(4) DEFAULT NULL,
  `diabetes` tinyint(4) DEFAULT NULL,
  `alcoholismo` tinyint(4) DEFAULT NULL,
  `displimedias` tinyint(4) DEFAULT NULL,
  `postMenopausia` tinyint(4) DEFAULT NULL,
  `terapiaReemplazoHormonal` tinyint(4) DEFAULT NULL,
  `Paciente_expediente` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `diagnostico`
--

CREATE TABLE `diagnostico` (
  `idDiagnostico` int(11) NOT NULL,
  `ingreso` tinyint(4) DEFAULT NULL,
  `dm` int(11) DEFAULT NULL,
  `hta` tinyint(4) DEFAULT NULL,
  `obesidad` tinyint(4) DEFAULT NULL,
  `dis` tinyint(4) DEFAULT NULL,
  `sindromeMetabolico` tinyint(4) DEFAULT NULL,
  `sobrepeso` tinyint(4) DEFAULT NULL,
  `deteccion` tinyint(4) DEFAULT NULL,
  `tratamientoPrevio` tinyint(4) DEFAULT NULL,
  `covid` tinyint(4) DEFAULT NULL,
  `Paciente_expediente` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `paciente`
--

CREATE TABLE `paciente` (
  `expediente` int(11) NOT NULL,
  `entNacimiento` varchar(45) DEFAULT NULL,
  `curp` varchar(16) DEFAULT NULL,
  `sexo` tinyint(4) DEFAULT NULL,
  `talla` int(11) DEFAULT NULL,
  `domicilio` varchar(150) DEFAULT NULL,
  `telefono` varchar(10) DEFAULT NULL,
  `spss` int(11) DEFAULT NULL,
  `fechaNac` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Volcado de datos para la tabla `paciente`
--

INSERT INTO `paciente` (`expediente`, `entNacimiento`, `curp`, `sexo`, `talla`, `domicilio`, `telefono`, `spss`, `fechaNac`) VALUES
(1, '1', '1', 1, 1, '1', '22332323', 1, '0000-00-00');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario`
--

CREATE TABLE `usuario` (
  `idUsuario` int(11) NOT NULL,
  `usuario` varchar(20) NOT NULL,
  `password` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Volcado de datos para la tabla `usuario`
--

INSERT INTO `usuario` (`idUsuario`, `usuario`, `password`) VALUES
(1, 'CarlosMZ', '12345'),
(2, 'MarioAD', '23456'),
(3, 'PabloOP', '34567');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `visita`
--

CREATE TABLE `visita` (
  `idcontrol` int(11) NOT NULL,
  `fecha` date DEFAULT NULL,
  `peso` double DEFAULT NULL,
  `talla` int(11) DEFAULT NULL,
  `trigliceridos` int(11) DEFAULT NULL,
  `glucemia` int(11) DEFAULT NULL,
  `HbA1c` double DEFAULT NULL,
  `revisionPies` double DEFAULT NULL,
  `controlado` tinyint(4) DEFAULT NULL,
  `ayudaMutua` tinyint(4) DEFAULT NULL,
  `complicaciones` tinyint(4) DEFAULT NULL,
  `referencia` tinyint(4) DEFAULT NULL,
  `baja` date DEFAULT NULL,
  `hdl` int(11) DEFAULT NULL,
  `ldl` int(11) DEFAULT NULL,
  `cintura` int(11) DEFAULT NULL,
  `sistolica` int(11) DEFAULT NULL,
  `diastolica` int(11) DEFAULT NULL,
  `noFarmacologico` varchar(15) DEFAULT NULL,
  `farmacologico` varchar(15) DEFAULT NULL,
  `observaciones` varchar(300) DEFAULT NULL,
  `Paciente_expediente` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `antecedentesfamiliares`
--
ALTER TABLE `antecedentesfamiliares`
  ADD PRIMARY KEY (`idantecentesFamiliares`,`Paciente_expediente`);

--
-- Indices de la tabla `antecedentespersonales`
--
ALTER TABLE `antecedentespersonales`
  ADD PRIMARY KEY (`idantecedentesPersonales`,`Paciente_expediente`);

--
-- Indices de la tabla `diagnostico`
--
ALTER TABLE `diagnostico`
  ADD PRIMARY KEY (`idDiagnostico`,`Paciente_expediente`);

--
-- Indices de la tabla `paciente`
--
ALTER TABLE `paciente`
  ADD PRIMARY KEY (`expediente`);

--
-- Indices de la tabla `usuario`
--
ALTER TABLE `usuario`
  ADD PRIMARY KEY (`idUsuario`);

--
-- Indices de la tabla `visita`
--
ALTER TABLE `visita`
  ADD PRIMARY KEY (`idcontrol`,`Paciente_expediente`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `paciente`
--
ALTER TABLE `paciente`
  MODIFY `expediente` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `usuario`
--
ALTER TABLE `usuario`
  MODIFY `idUsuario` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;