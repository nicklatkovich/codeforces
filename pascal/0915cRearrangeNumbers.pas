PROGRAM ReqarrangeNumbers;
USES math;
VAR a, b                                            : STRING;
    aNums, rNums, bNums                             : ARRAY OF BYTE;
    i, aLen, bLen, temp, j, ind, t1, lastInd, iFrom : BYTE;
    t2, isLess                                      : BOOLEAN;
    _0ord                                           : INTEGER;
BEGIN
    _0ord := Ord('0');
    ReadLn(a);
    Read(b);
    aLen := Length(a);
    bLen := Length(b);
    SetLength(aNums, 10);
    FOR i := 1 TO 10 DO aNums[i] := 0;
    FOR i := 1 TO aLen DO BEGIN
        temp := Ord(a[i]) - _0ord;
		IF (temp >= 0) AND (temp <= 9) THEN aNums[Max(temp, (temp + 10) MOD 11)] += 1;
    END;
    SetLength(bNums, bLen);
    FOR i := 1 TO bLen DO bNums[i] := Ord(b[i]) - _0ord;
    IF aLen <> bLen THEN BEGIN
        FOR i := 9 DOWNTO 0 DO BEGIN
            temp := Max(i, (i + 10) MOD 11);
            FOR j := 1 TO aNums[temp] DO Write(i);
        END;
    END ELSE BEGIN
        SetLength(rNums, aLen);
        ind := 0;
        isLess := false;
        lastInd := 0;
        FOR i := 1 TO aLen DO BEGIN
            temp := 0;
            IF isLess THEN iFrom := 9 ELSE iFrom := bNums[i];
            FOR j := iFrom DOWNTO 0 DO BEGIN
                t1 := Max(j, (j + 10) MOD 11);
                IF aNums[t1] > 0 THEN BEGIN
                    IF j < bNums[i] THEN BEGIN
                        isLess := true;
                        lastInd := i;
                    END;
                    ind := i;
                    rNums[i] := j;
                    Dec(aNums[t1]);
                    temp := 1;
                    BREAK;
                END;
            END;
            IF temp = 0 THEN BREAK;
        END;
        WHILE ind < aLen DO BEGIN
            t2 := true;
            IF isLess THEN iFrom := 9 ELSE iFrom := bNums[ind + 1];
            FOR i := iFrom DOWNTO 0 DO BEGIN
                t1 := Max(i, (i + 10) MOD 11);
                IF aNums[t1] > 0 THEN BEGIN
                    Dec(aNums[t1]);
                    Inc(ind);
                    rNums[ind] := i;
                    IF (NOT isLess) AND (i < iFrom) THEN BEGIN
                        isLess := true;
                        lastInd := ind;
                    END;
                    t2 := false;
                    BREAK;
                END;
            END;
            IF t2 THEN BEGIN
                Dec(ind);
                Inc(aNums[Max(temp, (temp + 10) MOD 11)]);
                IF isLess AND (ind = lastInd) THEN isLess := false;
            END;
        END;
        FOR i := 1 TO aLen DO Write(rNums[i]);
        WriteLn();
    END;
END.