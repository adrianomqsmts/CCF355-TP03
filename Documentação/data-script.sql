-- Inserindo Usuários de teste

INSERT INTO `onefigure`.`usuario` (`name`, `password`) VALUES ('teste', 'teste');
INSERT INTO `onefigure`.`usuario` (`name`, `password`) VALUES ('user', 'user');
INSERT INTO `onefigure`.`usuario` (`name`, `password`) VALUES ('fulano', 'fulano');
INSERT INTO `onefigure`.`usuario` (`name`, `password`) VALUES ('beltrano', 'beltrano');


-- Inserindo os dados das cartas

INSERT INTO `onefigure`.`figure` (`name`, `rarity`, `path`) VALUES ('Luffy 01', 'COMUM', 'img/luffy01.png');
INSERT INTO `onefigure`.`figure` (`name`, `rarity`, `path`) VALUES ('Luffy 02', 'COMUM', 'img/luffy02.png');
INSERT INTO `onefigure`.`figure` (`name`, `rarity`, `path`) VALUES ('Luffy 03', 'COMUM', 'img/luffy03.png');
INSERT INTO `onefigure`.`figure` (`name`, `rarity`, `path`) VALUES ('Luffy 04', 'RARA', 'img/luffy04.png');
INSERT INTO `onefigure`.`figure` (`name`, `rarity`, `path`) VALUES ('Luffy 05', 'ÉPICA', 'img/luffy05.png');
INSERT INTO `onefigure`.`figure` (`name`, `rarity`, `path`) VALUES ('Zoro 01', 'COMUM', 'img/zoro01.png');
INSERT INTO `onefigure`.`figure` (`name`, `rarity`, `path`) VALUES ('Zoro 02', 'COMUM', 'img/zoro02.png');
INSERT INTO `onefigure`.`figure` (`name`, `rarity`, `path`) VALUES ('Zoro 03', 'COMUM', 'img/zoro03.png');
INSERT INTO `onefigure`.`figure` (`name`, `rarity`, `path`) VALUES ('zoro 04', 'RARA', 'img/zoro04.png');
INSERT INTO `onefigure`.`figure` (`name`, `rarity`, `path`) VALUES ('Zoro 05', 'ÉPICA', 'img/zoro05.png');
INSERT INTO `onefigure`.`figure` (`name`, `rarity`, `path`) VALUES ('Sanji 01', 'COMUM', 'img/sanji01.png');
INSERT INTO `onefigure`.`figure` (`name`, `rarity`, `path`) VALUES ('Sanji 02', 'COMUM', 'img/sanji02.png');
INSERT INTO `onefigure`.`figure` (`name`, `rarity`, `path`) VALUES ('Sanji 03', 'COMUM', 'img/sanji03.png');
INSERT INTO `onefigure`.`figure` (`name`, `rarity`, `path`) VALUES ('Sanji 04', 'RARA', 'img/sanji04.png');
INSERT INTO `onefigure`.`figure` (`name`, `rarity`, `path`) VALUES ('Sanji 05', 'ÉPICA', 'img/sanji05.png');
INSERT INTO `onefigure`.`figure` (`name`, `rarity`, `path`) VALUES ('Nami 01', 'RARA', 'img/nami01.png');
INSERT INTO `onefigure`.`figure` (`name`, `rarity`, `path`) VALUES ('Nami 02', 'RARA', 'img/nami02.png');
INSERT INTO `onefigure`.`figure` (`name`, `rarity`, `path`) VALUES ('Nami 03', 'RARA', 'img/nami03.png');
INSERT INTO `onefigure`.`figure` (`name`, `rarity`, `path`) VALUES ('Nami 04 ', 'ÉPICA', 'img/nami04.png');
INSERT INTO `onefigure`.`figure` (`name`, `rarity`, `path`) VALUES ('Nami 05', 'ÉPICA', 'img/nami05.png');


-- Preenchendo o Álbum dos Jogadores

INSERT INTO `onefigure`.`album` (`idUser`, `idFigure`, `quantity`) VALUES ('2', '1', '3');
INSERT INTO `onefigure`.`album` (`idUser`, `idFigure`, `quantity`) VALUES ('2', '2', '2');
INSERT INTO `onefigure`.`album` (`idUser`, `idFigure`, `quantity`) VALUES ('2', '3', '1');
INSERT INTO `onefigure`.`album` (`idUser`, `idFigure`, `quantity`) VALUES ('2', '4', '1');
INSERT INTO `onefigure`.`album` (`idUser`, `idFigure`, `quantity`) VALUES ('2', '5', '1');
INSERT INTO `onefigure`.`album` (`idUser`, `idFigure`, `quantity`) VALUES ('2', '17', '1');
INSERT INTO `onefigure`.`album` (`idUser`, `idFigure`, `quantity`) VALUES ('2', '16', '2');
INSERT INTO `onefigure`.`album` (`idUser`, `idFigure`, `quantity`) VALUES ('2', '13', '2');
INSERT INTO `onefigure`.`album` (`idUser`, `idFigure`, `quantity`) VALUES ('2', '20', '5');
INSERT INTO `onefigure`.`album` (`idUser`, `idFigure`, `quantity`) VALUES ('3', '11', '3');
INSERT INTO `onefigure`.`album` (`idUser`, `idFigure`, `quantity`) VALUES ('3', '7', '5');
INSERT INTO `onefigure`.`album` (`idUser`, `idFigure`, `quantity`) VALUES ('3', '10', '2');
INSERT INTO `onefigure`.`album` (`idUser`, `idFigure`, `quantity`) VALUES ('3', '13', '3');
INSERT INTO `onefigure`.`album` (`idUser`, `idFigure`, `quantity`) VALUES ('3', '3', '3');
INSERT INTO `onefigure`.`album` (`idUser`, `idFigure`, `quantity`) VALUES ('3', '15', '15');
INSERT INTO `onefigure`.`album` (`idUser`, `idFigure`, `quantity`) VALUES ('3', '12', '10');
INSERT INTO `onefigure`.`album` (`idUser`, `idFigure`, `quantity`) VALUES ('4', '4', '4');
INSERT INTO `onefigure`.`album` (`idUser`, `idFigure`, `quantity`) VALUES ('4', '1', '3');
INSERT INTO `onefigure`.`album` (`idUser`, `idFigure`, `quantity`) VALUES ('4', '2', '2');
INSERT INTO `onefigure`.`album` (`idUser`, `idFigure`, `quantity`) VALUES ('4', '3', '3');
INSERT INTO `onefigure`.`album` (`idUser`, `idFigure`, `quantity`) VALUES ('4', '19', '1');
INSERT INTO `onefigure`.`album` (`idUser`, `idFigure`, `quantity`) VALUES ('4', '18', '2');
INSERT INTO `onefigure`.`album` (`idUser`, `idFigure`, `quantity`) VALUES ('4', '17', '2');
INSERT INTO `onefigure`.`album` (`idUser`, `idFigure`, `quantity`) VALUES ('4', '13', '2');
INSERT INTO `onefigure`.`album` (`idUser`, `idFigure`, `quantity`) VALUES ('4', '7', '2');



