package com.ltp.gradesubmission;
import java.util.Objects;

public class Grade {
    private String name;
    private String subject;
    private String score;


    public Grade() {
    }

    public Grade(String name, String subject, String score) {
        this.name = name;
        this.subject = subject;
        this.score = score;
    }

    public String getName() {
        return this.name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getSubject() {
        return this.subject;
    }

    public void setSubject(String subject) {
        this.subject = subject;
    }

    public String getScore() {
        return this.score;
    }

    public void setScore(String score) {
        this.score = score;
    }

    public Grade name(String name) {
        setName(name);
        return this;
    }

    public Grade subject(String subject) {
        setSubject(subject);
        return this;
    }

    public Grade score(String score) {
        setScore(score);
        return this;
    }

    @Override
    public boolean equals(Object o) {
        if (o == this)
            return true;
        if (!(o instanceof Grade)) {
            return false;
        }
        Grade grade = (Grade) o;
        return Objects.equals(name, grade.name) && Objects.equals(subject, grade.subject) && Objects.equals(score, grade.score);
    }

    @Override
    public int hashCode() {
        return Objects.hash(name, subject, score);
    }

    @Override
    public String toString() {
        return "{" +
            " name='" + getName() + "'" +
            ", subject='" + getSubject() + "'" +
            ", score='" + getScore() + "'" +
            "}";
    }
}