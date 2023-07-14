-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 14-07-2023 a las 11:36:00
-- Versión del servidor: 10.4.27-MariaDB
-- Versión de PHP: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `productos`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `productos`
--

CREATE TABLE `productos` (
  `id` int(3) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `precio` int(6) NOT NULL,
  `cantidad` int(2) NOT NULL,
  `categoria` varchar(50) NOT NULL,
  `foto` longblob NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `productos`
--

INSERT INTO `productos` (`id`, `nombre`, `precio`, `cantidad`, `categoria`, `foto`) VALUES
(4, 'Arpa', 150000, 10, 'cuerda', 0x52544b53453831514d3357414a30324e4c435a5f2e6a7067),
(5, 'Bateria', 205000, 5, 'percusion', 0x4333354f49443934364d374731324b5a544558572e6a7067),
(6, 'Guitarra electrica', 85000, 80, 'cuerda', 0x474e3252543957303834484543563544514258312e6a7067),
(7, 'Guitarra+estuche', 180000, 15, 'pack', 0x444e5442485538435731394d4a304559514746342e6a7067),
(8, 'saxofon', 320000, 30, 'aire', 0x4f555242415436475a4a4832563544573949434d2e6a7067),
(9, 'violin', 90000, 40, 'cuerda', 0x474c495648433436414b445f424e5155455357312e6a7067),
(10, 'guitarra pack', 54000, 30, 'pack', 0x5a5f4d343155563559395033464f4a47523630382e6a7067),
(11, 'guitarra acústica variedades', 32000, 150, 'cuerda', 0x4c544753493452503236514b35415a30464f48372e6a7067);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `users`
--

CREATE TABLE `users` (
  `id` int(10) NOT NULL,
  `email` varchar(50) NOT NULL,
  `username` varchar(30) NOT NULL,
  `password` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `users`
--

INSERT INTO `users` (`id`, `email`, `username`, `password`) VALUES
(1, 'alonso', '1234', 'al.villena@gmail.com'),
(2, 'richard', '1111', 'richard@gmail.com'),
(3, 'pato', '1111', 'pato123@gmail.com');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `productos`
--
ALTER TABLE `productos`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `productos`
--
ALTER TABLE `productos`
  MODIFY `id` int(3) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT de la tabla `users`
--
ALTER TABLE `users`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
