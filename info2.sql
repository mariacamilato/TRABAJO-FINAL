-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1:3306
-- Tiempo de generación: 31-05-2024 a las 05:42:24
-- Versión del servidor: 8.0.31
-- Versión de PHP: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `info2`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `enfermedades`
--

CREATE TABLE `enfermedades` (
  `ID` int UNSIGNED NOT NULL,
  `id_enfermedad` int UNSIGNED NOT NULL,
  `nombre` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `sintomas` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `especialista` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `tratamiento` varchar(100) COLLATE utf8mb4_general_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `enfermedades`
--

INSERT INTO `enfermedades` (`ID`, `id_enfermedad`, `nombre`, `sintomas`, `especialista`, `tratamiento`) VALUES
(1, 5, 'Alzheimer', 'Pérdida de memoria, desorientación, problemas del lenguaje, cambios en el comportamiento y la personalidad', 'Neurólogo', 'Memantina\ne Inhibidores de la colinesterasa'),
(2, 6, 'Agnosia Visual', 'Dificultad para identificar objetos, caras (prosopagnosia) o colores (acromatopsia)', 'Oftalmóloga o Neurólogo', 'puede ser rehabilitación, cirugía, antibióticos y/o radioterapia'),
(3, 7, 'Demencia frontotemporal', ' pueden presentar cambios en la personalidad, los síntomas varían entre interacción \ninapropiada socialmente, cambios emocionales, incapacidad de usar el lenguaje de forma coherente.', 'Neurólogo o geriatra', 'tratamiento psicológico y farmacológico'),
(4, 8, 'síndrome de Gerstman', 'incapacidad escribir, para operaciones matemáticas, confusión derecha izquierda e incapacidad de reconocer  dedos de manos a los de los pies. El tratamiento se orienta a terapia ocupacional y física e intervenciones psicoeducativas', 'Neurólogo', 'tratamiento psicológico, farmacológico y entrenamiento cognitivo'),
(5, 9, 'Ataxia cerebelosa', 'pérdida de coordinación y control muscular', 'Neurólogo y fisioterapeuta', 'Terapia física, muscular y del habla'),
(6, 10, 'síndrome de Wallenberg', 'Disfagia, Problemas de equilibrio y coordinación, Síndrome de Horner', 'Neurólogo y fisioterapeuta', 'terapia física y del habla, soporte nutricional y Medicamentos sintomáticos');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `general`
--

CREATE TABLE `general` (
  `ID` int UNSIGNED NOT NULL,
  `nombre` varchar(20) COLLATE utf8mb4_general_ci NOT NULL,
  `definicion` varchar(255) COLLATE utf8mb4_general_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `general`
--

INSERT INTO `general` (`ID`, `nombre`, `definicion`) VALUES
(1, 'Lóbulo temporal', 'El lóbulo temporal, ubicado cerca de las sienes, es esencial para la audición, el lenguaje, la memoria y el reconocimiento visual. Su buen funcionamiento es vital para las actividades diarias y su daño puede afectar la calidad de vida.'),
(2, 'Lóbulo occipital', 'El lóbulo occipital, localizado en la parte posterior del cerebro, es crucial para la interpretación y procesamiento de la información visual. Su correcto funcionamiento es esencial para la percepción consciente y la interpretación del entorno visual.'),
(3, 'Lóbulo frontal', ' Responsable de los procesos cognitivos complejos, son las funciones ejecutivas. Nos permite razonar, elegir, planificar, tomar decisiones, atención y lenguaje.'),
(4, 'Lóbulo parietal', 'Interpreta dolor, frío, calor, olfato gusto y tacto. Hemisferio izquierdo: los diestros, maneja simbología de letras y números. Hemisferio derecho: los zurdos, interpreta imágenes.'),
(5, 'cerebelo', 'Responsable de coordinar la fluidez de los movimientos, articulación de lenguaje escrito y oral.'),
(6, 'Tallo encefálico', 'Transmisión de la emergencia motora del lenguaje y alerta al organismo para permitir  activar la lingüística.');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `enfermedades`
--
ALTER TABLE `enfermedades`
  ADD PRIMARY KEY (`id_enfermedad`),
  ADD KEY `ID` (`ID`);

--
-- Indices de la tabla `general`
--
ALTER TABLE `general`
  ADD PRIMARY KEY (`ID`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `enfermedades`
--
ALTER TABLE `enfermedades`
  MODIFY `id_enfermedad` int UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de la tabla `general`
--
ALTER TABLE `general`
  MODIFY `ID` int UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `enfermedades`
--
ALTER TABLE `enfermedades`
  ADD CONSTRAINT `enfermedades_ibfk_1` FOREIGN KEY (`ID`) REFERENCES `general` (`ID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
