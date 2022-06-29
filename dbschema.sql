CREATE TABLE file (id TEXT PRIMARY KEY, date TEXT, section TEXT);
CREATE TABLE reference (id INTEGER PRIMARY KEY, reference TEXT);
CREATE TABLE sample (
    id TEXT PRIMARY KEY,
    file_id TEXT,
    `AGE` TEXT,
`ALTERATION` TEXT,
`DRILL_DEPTHAX` TEXT,
`DRILL_DEPTH_MIN` TEXT,
`ELEVATION_MAX` REAL,
`ELEVATION_MIN` REAL,
`EPSILON_ND` TEXT,
`ERUPTION_DAY` TEXT,
`ERUPTION_MONTH` TEXT,
`ERUPTION_YEAR` TEXT,
`GEOL.` TEXT,
`LAND_OR_SEA` TEXT,
`LATITUDE_MAX` REAL,
`LATITUDE_MIN` REAL,
`LOCATION` TEXT,
`LOCATION_COMMENT` TEXT,
`LONGITUDE_MAX` REAL,
`LONGITUDE_MIN` REAL,
`MATERIAL` TEXT,
`MINERAL` TEXT,
`ROCK_NAME` TEXT,
`ROCK_TEXTURE` TEXT,
`ROCK_TYPE` TEXT,
`TECTONIC_SETTING` TEXT,
`AR40_K40` REAL,
`HE3_HE4` REAL,
`HE4_HE3` REAL,
`HF176_HF177` REAL,
`K40_AR40` REAL,
`ND143_ND144` REAL,
`ND143_ND144_INI` REAL,
`OS184_OS188` REAL,
`OS186_OS188` REAL,
`OS187_OS186` REAL,
`OS187_OS188` REAL,
`PB206_PB204` REAL,
`PB206_PB204_INI` REAL,
`PB207_PB204` REAL,
`PB207_PB204_INI` REAL,
`PB208_PB204` REAL,
`PB208_PB204_INI` REAL,
`RE187_OS186` REAL,
`RE187_OS188` REAL,
`SR87_SR86` REAL,
`SR87_SR86_INI` REAL,
`AG(PPM)` REAL,
`AL(PPM)` REAL,
`AS(PPM)` REAL,
`AU(PPM)` REAL,
`B(PPM)` REAL,
`BA(PPM)` REAL,
`BE(PPM)` REAL,
`BI(PPM)` REAL,
`BR(PPM)` REAL,
`C(PPM)` REAL,
`CA(PPM)` REAL,
`CAO(WT%)` REAL,
`CD(PPM)` REAL,
`CE(PPM)` REAL,
`CL(PPM)` REAL,
`CL(WT%)` REAL,
`CO(PPM)` REAL,
`CR(PPM)` REAL,
`CS(PPM)` REAL,
`CU(PPM)` REAL,
`DY(PPM)` REAL,
`ER(PPM)` REAL,
`EU(PPM)` REAL,
`F(PPM)` REAL,
`F(WT%)` REAL,
`FE(PPM)` REAL,
`FEO(WT%)` REAL,
`FEOT(WT%)` REAL,
`GA(PPM)` REAL,
`GD(PPM)` REAL,
`GE(PPM)` REAL,
`HE(CCM/G)` REAL,
`HE(CCMSTP/G)` REAL,
`HE(NCC/G)` REAL,
`HF(PPM)` REAL,
`HG(PPM)` REAL,
`HO(PPM)` REAL,
`I(PPM)` REAL,
`IN(PPM)` REAL,
`IR(PPM)` REAL,
`K(PPM)` REAL,
`LA(PPM)` REAL,
`LI(PPM)` REAL,
`LOI(WT%)` REAL,
`LU(PPM)` REAL,
`MAX._AGE_(YRS.)` TEXT,
`MG(PPM)` REAL,
`MGO(WT%)` REAL,
`MIN._AGE_(YRS.)` TEXT,
`MN(PPM)` REAL,
`MNO(WT%)` REAL,
`MO(PPM)` REAL,
`NA(PPM)` REAL,
`NB(PPM)` REAL,
`ND(PPM)` REAL,
`NI(PPM)` REAL,
`NIO(WT%)` REAL,
`O(WT%)` REAL,
`OH(WT%)` REAL,
`OS(PPM)` REAL,
`OTHERS(WT%)` REAL,
`P(PPM)` REAL,
`PB(PPM)` REAL,
`PD(PPM)` REAL,
`PR(PPM)` REAL,
`PT(PPM)` REAL,
`RB(PPM)` REAL,
`RE(PPM)` REAL,
`RH(PPM)` REAL,
`RU(PPM)` REAL,
`S(PPM)` REAL,
`S(WT%)` REAL,
`SB(PPM)` REAL,
`SC(PPM)` REAL,
`SE(PPM)` REAL,
`SM(PPM)` REAL,
`SN(PPM)` REAL,
`SR(PPM)` REAL,
`TA(PPM)` REAL,
`TB(PPM)` REAL,
`TE(PPM)` REAL,
`TH(PPM)` REAL,
`TI(PPM)` REAL,
`TL(PPM)` REAL,
`TM(PPM)` REAL,
`U(PPM)` REAL,
`V(PPM)` REAL,
`VOLATILES(WT%)` REAL,
`W(PPM)` REAL,
`Y(PPM)` REAL,
`YB(PPM)` REAL,
`ZN(PPM)` REAL,
`ZR(PPM)` REAL,
`AL2O3(WT%)` REAL,
`B2O3(WT%)` REAL,
`CH4(WT%)` REAL,
`CL2(WT%)` REAL,
`CO1(WT%)` REAL,
`CO2(PPM)` REAL,
`CO2(WT%)` REAL,
`CR2O3(WT%)` REAL,
`FE2O3(WT%)` REAL,
`H2O(WT%)` REAL,
`H2OM(WT%)` REAL,
`H2OP(WT%)` REAL,
`H2OT(WT%)` REAL,
`HE3(AT/G)` REAL,
`HE3(CCMSTP/G)` REAL,
`HE3_HE4(R/R(A))` REAL,
`HE4(AT/G)` REAL,
`HE4(CCM/G)` REAL,
`HE4(CCMSTP/G)` REAL,
`HE4(MOLE/G)` REAL,
`HE4(NCC/G)` REAL,
`HE4_HE3(R/R(A))` REAL,
`K2O(WT%)` REAL,
`NA2O(WT%)` REAL,
`P2O5(WT%)` REAL,
`SIO2(WT%)` REAL,
`SO2(WT%)` REAL,
`SO3(WT%)` REAL,
`SO4(WT%)` REAL,
`TIO2(WT%)` REAL,
    FOREIGN KEY (file_id) REFERENCES file(id)
);
CREATE TABLE citation (
    sample_id TEXT,
    reference_id INTEGER,
    fields TEXT,
    FOREIGN KEY (sample_id) REFERENCES sample(id),
    FOREIGN KEY (reference_id) REFERENCES reference(id)
);
