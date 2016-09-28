<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
	<xsl:template match="/carrental">
		<html>
			<xsl:apply-templates/>
		</html>
	</xsl:template>

	<xsl:template match="rental">
			<head>
				<title><xsl:value-of select="marca"/> <xsl:value-of select="model"/></title>
			</head>
			<body>
				<h1><xsl:value-of select="marca"/></h1><br />
				<h2><xsl:value-of select="model"/></h2><br />
				<table border="0">
					<tr><td>VIN:</td><td><xsl:value-of select="@vin"/></td></tr>
					<tr><td>Start:</td><td><xsl:value-of select="start"/></td></tr>
					<tr><td>Fi:</td><td><xsl:value-of select="fi"/></td></tr>
				</table>
			</body>
	</xsl:template>

</xsl:stylesheet>


