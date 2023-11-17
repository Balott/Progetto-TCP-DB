-- phpMyAdmin SQL Dump
-- version 4.6.6deb5ubuntu0.5
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Creato il: Ott 03, 2023 alle 09:43
-- Versione del server: 5.7.40-0ubuntu0.18.04.1
-- Versione PHP: 7.2.24-0ubuntu0.18.04.15

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `5ATepsit`
--

-- --------------------------------------------------------

--
-- Struttura della tabella `zone_di_lavoro_francesco_balotta`
--

CREATE TABLE `zone_di_lavoro_francesco_balotta` (
  `id_zona` int(11) NOT NULL,
  `nome_zona` varchar(100) NOT NULL,
  `num_clienti` int(11) NOT NULL,
  `id_dipendente` int(11) DEFAULT NULL,
  `num_uffici` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dump dei dati per la tabella `zone_di_lavoro_francesco_balotta`
--

INSERT INTO `zone_di_lavoro_francesco_balotta` (`id_zona`, `nome_zona`, `num_clienti`, `id_dipendente`, `num_uffici`) VALUES
(1, '99', 2, 1, 45);

--
-- Indici per le tabelle scaricate
--

--
-- Indici per le tabelle `zone_di_lavoro_francesco_balotta`
--
ALTER TABLE `zone_di_lavoro_francesco_balotta`
  ADD PRIMARY KEY (`id_zona`),
  ADD KEY `id_dipendente` (`id_dipendente`);

--
-- AUTO_INCREMENT per le tabelle scaricate
--

--
-- AUTO_INCREMENT per la tabella `zone_di_lavoro_francesco_balotta`
--
ALTER TABLE `zone_di_lavoro_francesco_balotta`
  MODIFY `id_zona` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
--
-- Limiti per le tabelle scaricate
--

--
-- Limiti per la tabella `zone_di_lavoro_francesco_balotta`
--
ALTER TABLE `zone_di_lavoro_francesco_balotta`
  ADD CONSTRAINT `zone_di_lavoro_francesco_balotta_ibfk_1` FOREIGN KEY (`id_dipendente`) REFERENCES `clienti_francesco_balotta` (`id`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
