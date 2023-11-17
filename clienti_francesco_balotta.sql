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
-- Struttura della tabella `clienti_francesco_balotta`
--

CREATE TABLE `clienti_francesco_balotta` (
  `id` int(11) NOT NULL,
  `nome` varchar(100) NOT NULL,
  `cognome` varchar(100) NOT NULL,
  `pos_lavorativa` varchar(1024) NOT NULL,
  `data_assunzione` date NOT NULL,
  `telefono` int(255) DEFAULT NULL,
  `indirizzo_casa` varchar(1024) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dump dei dati per la tabella `clienti_francesco_balotta`
--

INSERT INTO `clienti_francesco_balotta` (`id`, `nome`, `cognome`, `pos_lavorativa`, `data_assunzione`, `telefono`, `indirizzo_casa`) VALUES
(1, 'boh', 'ciao', '123', '2023-09-01', 354, 'ciao');

--
-- Indici per le tabelle scaricate
--

--
-- Indici per le tabelle `clienti_francesco_balotta`
--
ALTER TABLE `clienti_francesco_balotta`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT per le tabelle scaricate
--

--
-- AUTO_INCREMENT per la tabella `clienti_francesco_balotta`
--
ALTER TABLE `clienti_francesco_balotta`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
